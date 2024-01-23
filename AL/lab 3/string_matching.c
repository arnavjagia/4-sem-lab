/*
Write a program to implement brute-force string matching. Analyze its time efficiency.
*/

#include <stdio.h>
#include <string.h>

// global opcount counter
int opcount = 0;

int string_match(char *str, char *substr)
{
    int len1 = strlen(str), len2 = strlen(substr);

    // if substr longer than str then bad
    if (len2>len1) { return -1; }

    for (int i=0; i<len1; ++i)
        // first character matches in string
        if (substr[0] == str[i])
            for (int j=1; j<len2; ++j)
            {
                ++opcount;
                if (substr[j] != str[i+j]) break;
                if (j+1 == len2) return i;
            }
    return -1;
}

int main()
{
    char str[] = " ";
    char substr[] = "World";

    string_match(str, substr);
    printf("\n%d\n", opcount);
    
    return 0;
}
/*

*/
