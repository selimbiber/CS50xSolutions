// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
#define TABLE_SIZE 50000

// Hash table
node *table[TABLE_SIZE];
int counter = 0; // Word count

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned int hashvalue = 0;
    for (int i = 0; word[i] != '\0'; i++)
    {
        hashvalue += tolower(word[i]);
        hashvalue = (hashvalue * 33 + tolower(word[i])) % TABLE_SIZE; // A simple hash function
    }
    return hashvalue;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index = hash(word);
    node *cursor = table[index];

    // Traverse the linked list
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
            return true;
        cursor = cursor->next;
    }
    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not load %s.\n", dictionary);
        return false;
    }

    char wordlist[LENGTH + 1];
    while (fscanf(file, "%s", wordlist) != EOF)
    {
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            fclose(file);
            return false; // Return false if memory allocation fails
        }

        strcpy(newNode->word, wordlist);
        newNode->next = NULL;

        int index = hash(wordlist);
        // Insert the new node into the hash table
        newNode->next = table[index];
        table[index] = newNode;

        counter++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return counter;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < TABLE_SIZE; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }
    return true;
}
