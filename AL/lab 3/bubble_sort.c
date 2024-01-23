/*
Write a program to sort set of integers using bubble sort. Analyze its time
efficiency. Obtain the experimental result of order of growth. Plot the result for
the best and worst case.
*/

#include <stdio.h>

// global opcount counter
int opcount = 0;

void swap (int *a, int *b)
{
    int t = *a; *a = *b; *b = t;
}

void bubble_sort(int *arr, unsigned int len)
{
    for (int i=0; i<len-1; i++)
        for (int j=0; j<len-i-1; j++)
        {
            opcount++;
            if (arr[j+1]<arr[j])
                swap(&arr[j+1], &arr[j]);
        }
}

int main() 
{
    int arr[] = {56,87,34,79,23,94,12,109,34};

    unsigned int len = sizeof(arr)/sizeof(arr[0]);
    
    bubble_sort(arr, len);
    
    for (int i=0; i<len; i++)
        printf("%d ", arr[i]);
    printf("\nlen: %d\nopcount: %d\n", len, opcount);
    
    return 0;
}

/*

*/
