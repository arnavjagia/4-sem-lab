/*
Write a program to implement brute-force string matching. Analyze its time efficiency.
*/

#include <stdio.h>

int string_match(char *str, char *substr)
{
    int len1 = 0, len2 = 0;

    while(str[len1++] != '\0'); len1--;
    while(substr[len2++] != '\0'); len2--;
    printf("\n%d", len1);
    printf("\n%d", len2);
}

int main()
{
    char str[] = " ";
    char substr[] = "World";

    string_match(str, substr);
    
    return 0;
}
/*

*/
