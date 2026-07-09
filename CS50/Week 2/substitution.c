#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


bool key_is_valid(string key);
void encrypt(string plaintext, string key);

int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    string key = argv[1];

    if (!key_is_valid(key))
    {
        printf("Invalid key\n");
        return 1;
    }

    string plaintext = get_string("What would you like to cipher: ");

    encrypt(plaintext, key);
    return 0;
}

bool key_is_valid(string key)
{
    if (strlen(key) != 26)
    {
        return false;
    }

    bool duplicate[26] = {false};

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        int index = toupper(key[i]) - 'A';

        if (duplicate[index])
        {
            return false;
        }
        duplicate[index] = true;

    }
    return true;
}

void encrypt(string plaintext, string key)
{
    printf("ciphertext: ");

    for (int i = 0, length =  strlen(plaintext); i < length; i++)
    {
        if (isupper(plaintext[i]))
        {
            int index = plaintext[i] - 'A';
            printf("%c", toupper(key[index]));
        }

        else if (islower(plaintext[i]))
        {
            int index = plaintext[i] - 'a';
            printf("%c", tolower(key[index]));
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }

    printf("\n");
}
