/*
Write a program to implement Horspool’s algorithm for String Matching and find
the number of key comparisons in successful search and unsuccessful search.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *shiftTable(char *pattern, int m) {
    int *table = malloc(128*sizeof(*table)); // Allocate memory for 128 ASCII characters
    for (int i=0; i<128; ++i)
        table[i] = m;
    for (int j=0; j<=m-2; ++j)
        table[(unsigned) pattern[j]]=m-j-1;
    return table;
}

int horspoolMatching(char *pattern, char *text, int m, int n) {
    // returns -1 if no match 
    int *table = shiftTable(pattern, m);
    int i = m-1;
    while (i<=n-1) {
        int k = 0;
        while (k<= m-1 && pattern[m-1-k]==text[i-k]) {
            ++k;
        }
        if (k==m) {
            return i-m+1;
        } else {
            i += table[(unsigned) text[i]];
        }
    }
    return -1;
}

int main()
{
    printf("pattern: ");
    char pattern[100];
    gets(pattern);
    printf("text: ");
    char text[100];
    gets(text);
    int leftIndexofFirstMatchedString = horspoolMatching(pattern, text, strlen(pattern), strlen(text));
    printf("String match found at %d\n", leftIndexofFirstMatchedString);
    return 0;
}

/* ---SAMPLE IO---
pattern: BARBER
text: JIM SAW ME IN A BARBERSHOP
String match found at 16
*/
