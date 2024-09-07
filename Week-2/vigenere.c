#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[]) {
    if (argc != 2) {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }

    string keyword = argv[1];

    for (int i = 0, n = strlen(keyword); i < n; i++) {
        if (!isalpha(keyword[i])) {
            printf("Invalid keyword. Please use only alphabetical characters.\n");
            return 1;
        }
    }

    // Anahtarın tamamını büyük harfe çevir
    int keyword_len = strlen(keyword);
    for (int i = 0; i < keyword_len; i++) {
        keyword[i] = toupper(keyword[i]);
    }

    string message = get_string("Enter the message: ");

    int ASCII_A = 65;
    int ascii_a = 97;
    int len_alphabet = 26;

    printf("ciphertext: ");

    int keyword_index = 0;
    int message_len = strlen(message);

    for (int i = 0; i < message_len; i++) {
        char keyword_map = keyword[keyword_index % keyword_len];

        if (isupper(message[i])) {
            printf("%c", ((message[i] - ASCII_A + (keyword_map - ASCII_A)) % len_alphabet + len_alphabet) % len_alphabet + ASCII_A);
            keyword_index++;
        } else if (islower(message[i])) {
            printf("%c", ((message[i] - ascii_a + (keyword_map - ASCII_A)) % len_alphabet + len_alphabet) % len_alphabet + ascii_a);
            keyword_index++;
        } else {
            printf("%c", message[i]);
        }
    }

    printf("\n");
    return 0;
}
