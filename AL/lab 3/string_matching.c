/*
Write a program to implement brute-force string matching. Analyze its time efficiency.
*/

#include <stdio.h>

int string_match(char *str, char *substr)
{
    int len1 = 0, len2 = 0;
    do {static int i=0; len1++} while (str[i] != '\0'); 
    do {static int i=0; len2++} while (substr[i] != '\0'); 
    printf("\n%ld", len1);
    printf("\n%ld", len2);
    // printf("\n%ld", sizeof(str));
    // printf("\n%ld", sizeof(substr));
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
