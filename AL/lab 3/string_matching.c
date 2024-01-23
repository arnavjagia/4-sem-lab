/*
Write a program to implement brute-force string matching. Analyze its time efficiency.
*/

#include <stdio.h>

int string_match(char str[], char substr[])
{
    printf("\n%ld", sizeof(str));
    printf("\n%ld", sizeof(substr));
}

int main()
{
    char str[] = "Hellooo";
    char substr[] = "World";
    printf("\n%ld", sizeof(str));
    printf("\n%ld", sizeof(substr));

    string_match(str, substr);
    
    return 0;
}
/*

*/
