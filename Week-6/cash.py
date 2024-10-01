from cs50 import get_float

def main():
    dollars = 0

    while dollars <= 0:
        dollars = get_float("Change owed: ")

    cents = round(dollars * 100)
    counter = 0

    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    while cents > 0:
        if cents >= quarter: 
            cents -= quarter
            counter += 1
        elif cents >= dime: 
            cents -= dime
            counter += 1
        elif cents >= nickel: 
            cents -= nickel
            counter += 1
        elif cents >= penny: 
            cents -= penny
            counter += 1

    print(f'Number of coins needed for the change: {counter}')

if __name__ == "__main__":
    main()