from cs50 import get_int 

def main():
    while True:
        height = get_int('Height: ')
        if height >= 1 and height <= 8:
            break
        else:
            print("Please enter a height between 1 and 8.")
            continue # Ask again in case of invalid input

    for i in range(1, height + 1):
        # Calculate the required number of spaces and # for each line
        spaces = height - i
        hashes = i
        print(' ' * spaces + '#' * hashes)

if __name__ == "__main__": 
    main()