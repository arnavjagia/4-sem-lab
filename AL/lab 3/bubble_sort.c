/*
Write a program to sort set of integers using bubble sort. Analyze its time
efficiency. Obtain the experimental result of order of growth. Plot the result for
the best and worst case.
*/

#include <stdio.h>

void swap (int *a, int *b)
{
    int t = *a; *a = *b; *b = t;
}

void bubble_sort(int *arr, unsigned int len)
{
    for (int i=0; i<len-1; i++)
        for (int j=i; j<len-1; j++)
            if (arr[j+1]<arr[j])
                swap(&arr[j+1], &arr[j]);
}

int main() 
{
    int setofintegers[] = {56,87,34,79,23,94};
    unsigned int len = sizeof(setofintegers)/sizeof(setofintegers[0]);
    bubble_sort(setofintegers, len);
    return 0;
}

/*

*/
