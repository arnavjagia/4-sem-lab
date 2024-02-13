#include <stdio.h>
#include <stdlib.h>
int count=0;
void merge(int *array_a, int *array_b, int *array_c, int n)
{
    int n_b = n / 2;
    int n_C = n - n_b;
    int i = 0, j = 0, k = 0;
    while (i < n_b && j < n_C)
    {
        if (array_b[i] <= array_c[j])
        {
            array_a[k] = array_b[i];
            k += 1;
            i += 1;
        }
        else
        {
            array_a[k] = array_c[j];
            k += 1;
            j += 1;
        }
    }
    if (i == n_b)
    {
        while (j < n_C)
        {
            array_a[k] = array_c[j];
            k += 1;
            j += 1;
        }
    }
    else
    {
        while (i < n_b)
        {
            array_a[k] = array_b[i];
            k += 1;
            i += 1;
        }
    }
    return;
}
void mergesort(int *arr, int n)
{
    if (n > 1)
    {
        int *arr_b = (int *)malloc(sizeof(int) * (n / 2));
        int *arr_c = (int *)malloc(sizeof(int) * (n - (n / 2)));
        int i = 0;
        for (int j = 0; i < n / 2; ++i, ++j)
        {
            arr_b[j] = arr[i];
            count++;
        }
        for (int j = 0; i < n; ++i, ++j)
        {
            arr_c[j] = arr[i];
            count++;
        }
        mergesort(arr_b, n / 2);
        mergesort(arr_c, n - (n / 2));
        merge(arr, arr_b, arr_c, n);
        count++;
    }
}
void main()
{
    int n, i;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int * arr = (int *) malloc(n * sizeof(int));
    for(i = 0; i < n; i++) {
        printf("Enter arr[%d]: ", i);
        scanf("%d", &arr[i]);
    }
    printf("Sorted array: ");
    mergesort(arr,n);
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\nOperations count: %d\n",count);
}