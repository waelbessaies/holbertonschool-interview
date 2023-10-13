#include "palindrome.h"
/**
 * is_palindrome - check if given number is palindrome or not
 * @n: number entered by user
 * Return: return 1 if n is a palindrome 0 otherwise
 */

int is_palindrome(unsigned long n)
{
    unsigned long reversed = 0, remainder, original;

    original = n;

    while (n != 0)
    {
        remainder = n % 10;
        reversed = reversed * 10 + remainder;
        n /= 10;
    }

    if (original == reversed)
        return (1);

    return (0);
}
