#include <stdio.h>
#include <cs50.h>

// Prototypes
bool validate_card(long number);
int get_digit_count(long number);
int get_first_two_digits(long number);

int main(void) {
    long number = get_long("Enter credit card number: ");

    // Validate the card number
    if (validate_card(number)) {
        int digits_count = get_digit_count(number);
        int first_two_digits = get_first_two_digits(number);

        // Determine the card type
        if (digits_count == 15 && (first_two_digits == 34 || first_two_digits == 37)) {
            printf("AMEX\n");
        } else if (digits_count == 16 && (first_two_digits >= 51 && first_two_digits <= 55)) {
            printf("MASTERCARD\n");
        } else if ((digits_count == 13 || digits_count == 16) && (first_two_digits / 10 == 4)) {
            printf("VISA\n");
        } else {
            printf("INVALID\n");
        }
    } else {
        printf("INVALID\n");
    }

    return 0;
}

// Function to validate card number using Luhn algorithm
bool validate_card(long number) {
    int sum = 0;
    bool alternate = false;

    while (number > 0) {
        int digit = number % 10;
        number /= 10;

        if (alternate) {
            digit *= 2;
            if (digit > 9) digit -= 9;
        }

        sum += digit;
        alternate = !alternate;
    }

    return (sum % 10 == 0);
}

// Function to get the number of digits in the card number
int get_digit_count(long number) {
    int count = 0;

    while (number > 0) {
        number /= 10;
        count++;
    }

    return count;
}

// Function to get the first two digits of the card number
int get_first_two_digits(long number) {
    while (number >= 100) {
        number /= 10;
    }

    return number;
}
