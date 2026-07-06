#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);

int main(void)
{
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int quarters = calculate_quarters(cents);

    cents = cents - (quarters * 25);

    int dimes = calculate_dimes(cents);

    cents = cents - (dimes * 10);

    int nickel = calculate_nickels(cents);

    cents = cents - (nickel * 5);

    int change = (cents + nickel + dimes + quarters);

    printf("%i\n", change);
     // printf("You are owed %i quarters, %i dimes, %i nickels abd %i cents\n", quarters, dimes, nickel, cents);
}

// Functions

int calculate_quarters(int cents)
{
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes = 0;
    while (cents >= 10)
    {
        dimes++;
        cents = cents - 10;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickel = 0;
    while (cents >= 5)
    {
        nickel++;
        cents = cents - 5;
    }
    return nickel;
}
