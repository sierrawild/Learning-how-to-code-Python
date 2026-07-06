#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// list of the alphabet maped to points
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int calculate_score(string word);

int main(void)
{

    // prompts player 1
    string word1 = get_string("Player 1: ");
    // prompts player 2
    string word2 = get_string("Player 2: ");

    // compute the score and compare
    int score1 = calculate_score(word1);
    int score2 = calculate_score(word2);

    // anounce the winer
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int calculate_score(string word)
{
    int score = 0;

    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
        if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }
    return score;
}
