// performing merge sort on an array
#include <stdio.h>
#include <stdlib.h>

void merge(int *b, int *c, int *a, int n)
{
    int i = 0, j = 0, k = 0;
    int p = n / 2, q = n / 2;
    while (i < p && j < q)
    {
        if (b[i] <= c[j])
            a[k++] = b[i++];
        else if (c[j] < b[i])
            a[k++] = c[j++];
    }
    if (i == p)
    {
        while (j == q)
        {
            a[k++] = c[j++];
        }
    }
    else
    {
        while (i == p)
        {
            a[k++] = b[i++];
        }
    }
}

void mergesort(int *a, int n)
{
    if (n > 1)
    {
        int *b = malloc((n / 2) * sizeof(int));
        int *c = malloc((n / 2) * sizeof(int));
        int i = 0;
        while (i <= (n / 2) - 1)
        {
            b[i] = a[i];
            ++i;
        }
        int j = 0;
        while (i <= n - 1)
        {
            c[j] = a[i];
            ++i;
            ++j;
        }

        mergesort(b, n / 2);
        mergesort(c, n / 2);
        merge(b, c, a, n);

        for (int f = 0; f < (n / 2); ++f)
            printf("%d ", b[f]);
        printf("\nIn mergesort\n");
        for (int f = 0; f < (n / 2) + 1; ++f)
            printf("%d ", c[f]);
    }
}

int main()
{
    int arr[] = {2, 18, 23, 9, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    printf("\n\n");
    mergesort(arr, n);
    printf("\n\nAfter sort\n");
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    return 0;
}