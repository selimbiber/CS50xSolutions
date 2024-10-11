from sys import argv, exit
from cs50 import get_string

def main():
    if len(argv) != 2:
        print("Usage: python vigenere.py key (key is not a number or space character)")
        exit(1)

    keyword = argv[1]

    # Check if the key is a number or space character
    if keyword.strip() == "" or not keyword.isalpha():
        print("Key cannot be a number or space character.")
        exit(1)

    # Convert the entire key to uppercase
    keyword = keyword.upper()

    message = get_string("Enter the message: ")

    ASCII_A = 65
    ascii_a = 97
    len_alphabet = 26

    print("ciphertext: ", end="")

    keyword_index = 0
    message_len = len(message)

    for i in range(message_len):
        if keyword_index >= len(keyword):
            keyword_index = 0  # Start the keyword loop

        keyword_map = keyword[keyword_index]

        if message[i].isupper():
            print(chr((ord(message[i]) - ASCII_A + (ord(keyword_map) - ASCII_A)) % len_alphabet + ASCII_A), end="")
            keyword_index += 1
        elif message[i].islower():
            print(chr((ord(message[i]) - ascii_a + (ord(keyword_map) - ASCII_A)) % len_alphabet + ascii_a), end="")
            keyword_index += 1
        else:
            print(message[i], end="")  # Print other characters as they are

    print()  # Move to a new line

if __name__ == "__main__":
    main()
