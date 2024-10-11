from sys import argv, exit
from cs50 import get_string

def main():
    if len(argv) != 2:
        print("Usage: python caesar.py key (where key is a non-negative integer)")
        exit(1)

    try:
        key = int(argv[1])
        if key < 0:
            raise ValueError("Key must be a non-negative integer.")
    except ValueError:
        print("Key must be a non-negative integer.")
        exit(1)

    plaintext = get_string("plaintext: ")

    print("ciphertext: ", end="")

    for char in plaintext:
        if not char.isalpha():
            print(char, end="")
            continue

        ascii_offset = 65 if char.isupper() else 97

        pi = ord(char) - ascii_offset
        ci = (pi + key) % 26

        print(chr(ci + ascii_offset), end="")

    print()

    return 0

if __name__ == "__main__":
    main()