/*
Write a program to create a heap for the list of integers using top-down heap
construction algorithm and analyze its time efficiency. Obtain the experimental
results for order of growth and plot the result.
*/

#include <stdio.h>

int count = 0;

void heapify(int h[], int n) {
    int i, k, v, heapify, j;
    for (i = (n / 2); i >= 1; i--) {
        k = i;
        v = h[k];
        heapify = 0;
        while (heapify == 0 && 2 * k <= n) {
            count += 1;
            j = 2 * k;
            if (j < n)
                if (h[j] < h[j + 1]) j = j + 1;
            if (v >= h[j])
                heapify = 1;
            else {
                h[k] = h[j];
                k = j;
            }
        }
        h[k] = v;
    }
    return;
}

int main() {
    int h[20], i, n;
    printf("\nEnter the number of Elements:");
    scanf("%d", &n);
    printf("\nEnter the Elements:");
    for (i = 1; i <= n; i++)
        scanf("%d", &h[i]);
    printf("\ndisplay the array: ");
    for (i = 1; i <= n; i++) {
        printf("\t%d", h[i]);
    }
    heapify(h, n);
    printf("\nThe heap created: ");
    for (i = 1; i <= n; i++) {
        printf("\t%d", h[i]);
    }
    printf("\nopcount: %d", count);

    return 0;
}

/* ---SAMPLE IO---
Enter heap elements, -1 to stop: 2 3 1 5 4 -1
Heap: 1 3 2 5 4 

opcount: 1
*/
