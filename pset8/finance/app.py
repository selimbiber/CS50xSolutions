import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd, format_stock_prices

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    stock_data = db.execute(
        "SELECT symbol, SUM(shares) shares, price, SUM(total_price) total_price FROM \
        stocks WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])

    user_data = db.execute(
        "SELECT cash FROM users WHERE id = ?", session["user_id"])
    account_data = db.execute(
        "SELECT SUM(total_price) paid FROM stocks WHERE user_id = ?", session["user_id"])
    total_cash = user_data[0]['cash']

    if account_data[0]['paid']:
        total_cash = account_data[0]['paid'] + user_data[0]['cash']

    stock_data = format_stock_prices(stock_data)

    return render_template("index.html",
                           stocks=stock_data,
                           cash=usd(user_data[0]['cash']),
                           total=usd(total_cash))
    
@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow user to change their password"""
    if request.method == "POST":
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirmation = request.form.get("confirmation")

        # Validate input fields
        if not current_password:
            return apology("You must provide your current password!", 400)
        if not new_password:
            return apology("You must provide a new password!", 400)
        if new_password != confirmation:
            return apology("New password and confirmation must match!", 400)

        # Fetch user data from the database
        user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        # Check if the current password is correct
        if not check_password_hash(user[0]["hash"], current_password):
            return apology("Current password is incorrect!", 400)

        # Hash the new password and update it in the database
        new_hash = generate_password_hash(new_password)

        db.execute("UPDATE users SET hash = ? WHERE id = ?", new_hash, session["user_id"])

        flash("Password changed successfully!")
        return redirect("/")

    return render_template("change_password.html")
    
@app.route("/add", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to user's account"""
    if request.method == "POST":
        amount = request.form.get("amount")
        
        # Check if the amount is valid
        if not amount or not amount.isdigit() or int(amount) <= 0:
            return apology("Invalid amount entered", 400)

        current_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        
        new_cash = current_cash + int(amount)
        
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, session["user_id"])

        flash(f"Successfully added ${amount} to your account!")

        return redirect("/")

    return render_template("add.html")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol")
        if not shares:
            return apology("must provide shares")
        if not shares.isdigit():
            return apology("num of shares not valid")

        shares = int(float(shares))

        if shares <= 0:
            return apology("num of shares not valid")

        stock_data = lookup(symbol)

        if not stock_data:
            return apology("Symbol not found")

        user_data = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"])

        total_price = stock_data['price'] * shares
        cash = user_data[0]["cash"] - total_price

        if user_data[0]["cash"] < total_price:
            return apology("Not enough cash to complete the purchase")

        db.execute(
            "INSERT INTO stocks (user_id, symbol, price, shares, total_price) \
            VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            stock_data['symbol'],
            stock_data['price'],
            shares, total_price
        )
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   cash, session["user_id"])

        flash("Purchase completed successfully!")

        return redirect("/")

    return render_template("buy.html")

@app.route("/check", methods=["GET"])
def check():
    """Return true if username is available, else false, in JSON format"""
    username = request.args.get("username")

    # Ensure username was provided
    if not username:
        return jsonify({"error": "Missing username"}), 400

    # Check if the username already exists in the database
    rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

    # If a user with this username already exists, return false
    if len(rows) > 0:
        return jsonify({"available": False})
    else:
        return jsonify({"available": True})

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    stock_data = db.execute(
        "SELECT symbol, shares, price, total_price, date_created \
         FROM stocks WHERE user_id = ?", session["user_id"])

    stock_data = format_stock_prices(stock_data)

    return render_template("history.html", stocks=stock_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        
        if not symbol:
            return apology("You must provide a stock symbol.")
        
        quote = lookup(symbol)
        
        if quote is None:
            return apology("Invalid stock symbol.", 400)
        
        return render_template("quote.html", quote=quote)
    
    return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    
    if request.method == 'GET':
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("You must provide a username!")
        if not password:
            return apology("You must provide a password!")
        if not confirmation:
            return apology("You must confirm your password!")
        if password != confirmation:
            return apology("Passwords must match!")

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)

            rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

            session["user_id"] = rows[0]["id"]

            flash("Registered successfully!")
            return redirect("/")
        
        except Exception as e:
            if 'UNIQUE constraint failed' in str(e):
                return apology("Username already exists, please choose a different one.")
            return apology(f"Error: {str(e)}", 400)

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("Must provide symbol!")
        if not shares:
            return apology("Must provide shares!")
        if int(shares) <= 0:
            return apology("Num of shares not valid!")

        stock_data = lookup(symbol)

        if not stock_data:
            return apology("Symbol not found!")

        user_data = db.execute(
            "SELECT SUM(s.shares) shares, SUM(s.total_price) price, u.cash FROM users u \
            inner join stocks s on s.user_id = u.id WHERE u.id = ? \
            and symbol = ? GROUP BY s.symbol, u.cash",
            session["user_id"],
            symbol)

        if not user_data:
            return apology("Symbol not found!")

        shares = int(shares)
        if user_data[0]['shares'] < shares:
            return apology("Not enough shares to complete the sale!")

        total_price = stock_data['price'] * shares
        new_cash = total_price + user_data[0]['cash']

        db.execute(
            "INSERT INTO stocks (user_id, symbol, price, shares, total_price) \
            VALUES (?, ?, ?, ?, ?)",
            session["user_id"],
            stock_data['symbol'],
            stock_data['price'],
            shares * -1,
            total_price * -1
        )
        db.execute("UPDATE users SET cash = ? WHERE id = ?",
                   new_cash, session["user_id"])

        flash("Sale completed successfully!")

        return redirect("/")

    user_stocks = db.execute(
        "SELECT DISTINCT symbol FROM stocks s WHERE s.user_id = ?", session["user_id"])

    return render_template("sell.html", stocks=user_stocks)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()

    # Log the error details for debugging
    print(f"Error: {e.name} - {e.code}")
    print(f"Details: {str(e)}")
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run(debug=True)