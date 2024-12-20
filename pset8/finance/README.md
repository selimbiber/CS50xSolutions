# C$50 Finance

C$50 Finance is a personal finance management web application inspired by [CS50 Finance](https://finance.cs50.net/). It allows users to track their stock portfolios, make buy/sell transactions, add cash to their account, and view their transaction history. It is built using **Flask** as the backend framework, **SQLite** for database management, and **Bootstrap** for responsive front-end design.

This application is currently live and accessible at:  
[https://c-50-finance-project.onrender.com/)](https://c-50-finance-project.onrender.com/)

---

## Features

- **User Authentication**: Register, log in, and log out functionality.
- **Portfolio Management**: View portfolio, current stock holdings, and cash balance.
- **Buy and Sell Stocks**: Purchase and sell stocks by providing the stock symbol and the number of shares.
- **Transaction History**: View the history of your stock purchases and sales.
- **Add Cash**: Add funds to your account balance to purchase more stocks.
- **Change Password**: Securely change your account password.

---

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Bootstrap 4)
- **Database**: SQLite
- **APIs**: Stock market data is fetched from a public API (e.g., Yahoo Finance or similar).
- **Security**: Password hashing with `werkzeug.security` (using bcrypt).

---

## Requirements

Before running the project locally, make sure you have Python 3.x installed, along with the following dependencies:

- Flask
- CS50 (for SQLite database interaction)
- Werkzeug (for password hashing)
- jinja2 (templating engine)

### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Or you can manually install each dependency:

```bash
pip install flask
pip install cs50
pip install werkzeug
```

---

## Setup

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/selimbiber/CS50xSolutions/
   cd pset8\finance
   ```

2. **Database Setup**

   The project uses an SQLite database. To initialize it, run the following command to create the necessary tables:

   ```bash
   python create_db.py
   ```

   This script creates the `finance.db` database file with the necessary tables (`users`, `stocks`, etc.).

3. **Run the Application**

   To start the application, simply run:

   ```bash
   python app.py
   ```

   The app will run on `http://localhost:5000/` by default.

4. **Database Configuration**

   The app uses SQLite for data storage, and the database file is `finance.db`. You can open and inspect the database using any SQLite tool if needed.

---

## Features Overview

### 1. **Homepage**
   After logging in, users can see their portfolio of stocks, including the number of shares, the total value of the stocks, and available cash.

### 2. **Buy Stocks**
   Users can purchase stocks by entering a stock symbol and the number of shares. The app will display the stock price and calculate the total price for the shares. If the user has enough cash, the purchase will be completed, and the stock will be added to the portfolio.

### 3. **Sell Stocks**
   Users can sell stocks from their portfolio by selecting a stock symbol and specifying the number of shares they wish to sell. The app will calculate the total sale price and update the user's cash balance accordingly.

### 4. **Transaction History**
   Users can view a history of all their stock purchases and sales, including the stock symbol, price, number of shares, and transaction date.

### 5. **Add Cash**
   Users can add cash to their account by specifying an amount. This balance can then be used to buy more stocks.

### 6. **Change Password**
   Users can change their password securely. This feature requires the user to input their current password and confirm the new password.

---

## How to Use

### Register an Account

1. Navigate to the **Register** page.
2. Provide a username and password, and confirm your password.
3. Once registered, you will be logged in automatically.

### Log In

1. If you have already registered, navigate to the **Login** page.
2. Enter your username and password to access your account.

### Manage Portfolio

- On the homepage, you can see your portfolio's value, available cash, and the list of stocks you own.
- You can **buy** or **sell** stocks by selecting a stock symbol and the number of shares.
  
### Change Password

1. Navigate to the **Change Password** page from the navigation bar.
2. Provide your current password, a new password, and confirm it.
3. Your password will be updated in the system.

### Logout

To log out, simply click the **Log Out** button in the navigation bar.

---

## Contributing

Contributions are welcome! If you find a bug or want to add new features, feel free to fork the repository and submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to your forked repository (`git push origin feature-name`).
6. Create a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Flask**: For building the web framework.
- **Bootstrap**: For responsive and modern front-end design.
- **SQLite**: For lightweight database management.
- **CS50 Library**: For database interactions.
- **Werkzeug**: For secure password handling.
- **Public Stock APIs**: For stock market data.

---

## Contact

If you have any questions or suggestions, feel free to open an issue on GitHub or contact me at [selimbiber.dev@outlook.com](mailto: selimbiber.dev@outlook.com).