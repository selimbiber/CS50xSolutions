from cs50 import get_int

def main():
    number = get_int("Enter credit card number: ")

    # Validate the card number
    if validate_card(number):
        digits_count = get_digit_count(number)
        first_two_digits = get_first_two_digits(number)

        # Determine the card type
        if digits_count == 15 and (first_two_digits == 34 or first_two_digits == 37):
            print("AMEX")
        elif digits_count == 16 and (51 <= first_two_digits <= 55):
            print("MASTERCARD")
        elif (digits_count == 13 or digits_count == 16) and first_two_digits // 10 == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")

# Function to validate card number using Luhn algorithm
def validate_card(number):
    total_sum = 0
    alternate = False

    while number > 0:
        digit = number % 10
        number //= 10

        if alternate:
            digit *= 2
            digit -= 9 if digit > 9 else 0

        total_sum += digit
        alternate = not alternate

    return total_sum % 10 == 0

# Function to get the number of digits in the card number
def get_digit_count(number):
    count = 0

    while number > 0:
        number //= 10
        count += 1

    return count

# Function to get the first two digits of the card number
def get_first_two_digits(number):
    while number >= 100:
        number //= 10

    return number

if __name__ == "__main__":
    main()
