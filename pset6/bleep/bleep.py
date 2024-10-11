import sys
from cs50 import get_string

def main():
    # Check the command line argument
    if len(sys.argv) != 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)

    # Load the banned words from the file
    banned_words = load_banned_words(sys.argv[1])

    message = get_string("Enter a message: ")

    censored_message = censor_message(message, banned_words)

    print(censored_message)

def load_banned_words(filename):
    """Read banned words from the file and store them in a set."""
    banned = set()  # Use a set to store the words
    with open(filename, 'r') as file:
        for line in file:
            banned.add(line.strip().lower())  # Store in lowercase
    return banned

def censor_message(message, banned_words):
    """Censor the banned words in the message."""
    words = message.split()
    for i in range(len(words)):
        # Check the lowercase version of the word against the banned words
        if words[i].lower() in banned_words:
            # Replace the word with '*' based on its length
            words[i] = '*' * len(words[i])
    return ' '.join(words)

if __name__ == "__main__":
    main()
