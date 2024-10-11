#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[]) {
    if (argc != 2) {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);
    
    if (key < 0) {
        printf("Key must be a non-negative integer.\n");
        return 1;
    }

    string message = get_string("Enter the message: ");

    int ASCII_A = 65;
    int ascii_a = 97;
    int len_alphabet = 26;

    printf("ciphertext: ");

    int n = strlen(message);

    for (int i = 0; i < n; i++) {
        if (isupper(message[i]))
            printf("%c", ((message[i] - ASCII_A + key) % len_alphabet + len_alphabet) % len_alphabet + ASCII_A);

        else if (islower(message[i]))
            printf("%c", ((message[i] - ascii_a + key) % len_alphabet + len_alphabet) % len_alphabet + ascii_a);

        else
            printf("%c", message[i]);
    }

    printf("\n");
    return 0;
}
