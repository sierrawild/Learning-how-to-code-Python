#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    for (int i = 0; i < n; i++)
    {
        print_row(n - i - 1, i + 1);
    }
}

void print_row(int spaces, int bricks)
{

    for (int i = 0; i < spaces; i++)
    {
        printf(" ");
    }
    for (int j = 0; j < bricks; j++)
    {
        printf("#");
    }
    printf("  ");
    for (int j = 0; j < bricks; j++)
    {
        printf("#");
    }
    printf("\n");
}
