/*
Sort given set of integers using Quick sort and analyze its efficiency. Obtain the
experimental result of order of growth and plot the result.
*/

#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

int partition(int *a, int l, int r) {
    int p = a[l];
    int i = l, j = r+1;

    while (i < j)  {
        for (; a[i] >= p; ++i);
        for (; a[j] <= p; --j);
        swap(&a[i], &a[j]);
    }

    swap(&a[i], &a[j]);
    swap(&a[l], &a[j]);

    return j;
}

void quick_sort(int *a, int l, int r) {
    if (l<r) {
        int s = partition(a, l, r);
        quick_sort(a, l, s-1);
        quick_sort(a, s+1, r);
    }
}

void display(int *a, int length) {
    for (int i=0; i<length; ++i)
        printf("%d ", a[i]);
    printf("\n");
}

int main() {
    int arr[] = {2, 18, 23, 9, 6};
    int n = sizeof(arr)/ sizeof(arr[0]);
    quick_sort(arr, 0, n-1);
    return 0;
}