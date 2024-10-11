#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void) {
    float dollars;

    do {
        dollars = get_float("Change owed: ");
    } while (dollars < 0);

    int cents = round(dollars * 100);
    int counter = 0;

    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int penny = 1;

    while (cents > 0) {
        if (cents >= quarter) {
            cents -= quarter;
            counter++;
        } else if (cents >= dime) {
            cents -= dime;
            counter++;
        } else if (cents >= nickel) {
            cents -= nickel;
            counter++;
        } else if (cents >= penny) {
            cents -= penny;
            counter++;
        }
    }

    printf("Number of coins needed for the change: %i \n", counter);

    return 0;
}
