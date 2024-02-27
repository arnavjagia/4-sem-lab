// performing merge sort on an array
#include <stdio.h>
#include <stdlib.h>

void merge(int *b, int *c, int *a, int p, int q) {
    int i = 0, j = 0, k = 0;
    while (i < p && j < q) {
        if (b[i] <= c[j])
            a[k++] = b[i++];
        else
            a[k++] = c[j++];
    }
    while (i < p)
        a[k++] = b[i++];
    while (j < q)
        a[k++] = c[j++];
}

void mergesort(int *a, int n) {
    if (n > 1) {
        int p = n / 2;
        int q = n - p;
        int *b = malloc(p * sizeof(int));
        int *c = malloc(q * sizeof(int));
        for (int i = 0; i < p; ++i)
            b[i] = a[i];
        for (int i = p; i < n; ++i)
            c[i - p] = a[i];

        mergesort(b, p);
        mergesort(c, q);
        merge(b, c, a, p, q);

        free(b);
        free(c);
    }
}

int main() {
    int arr[] = {2, 18, 23, 9, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Before sorting:\n");
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n\n");

    mergesort(arr, n);

    printf("After sorting:\n");
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    
    return 0;
}
