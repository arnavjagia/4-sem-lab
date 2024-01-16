/*
Write a program to find GCD using consecutive integer checking method and analyze its time efficiency.
*/
#include <stdio.h>

// opcount
int opcount = 0;

int gcd(int num1, int num2)
{
    int small = (num1<num2) ? num1: num2;
    for (int divisor = small; divisor>=2 ; divisor--)
    {
        opcount+=1;
        if (num1%divisor==0 && num2%divisor==0)
        {
            return divisor;
        }
    }

    // if there is no common divisor
    return 1;
}

int main()
{
    int a, b;
    printf("Enter a and b: ");
    scanf("%d %d", &a, &b);
    printf("\nGCD is: %d", gcd(a, b));
    printf("\nopcount: %d", opcount);

    return 0;
}

/*
Enter a and b: 91 49

GCD is: 7
opcount: 43
*/
