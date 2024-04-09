#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

void heapify(int *arr, int n, int i)
{
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;
    if (l < n && arr[l] > arr[largest])
        largest = l;
    if (r < n && arr[r] > arr[largest])
        largest = r;
    if (largest != i)
    {
        swap(&arr[largest], &arr[i]);
        heapify(arr, n, largest);
    }
}

void bottom_up(int *arr, int n)
{
    int parent = n / 2 - 1;
    for (int i = parent; i >= 0; --i)
        heapify(arr, n, i);
}

void display(int *arr, int n) {
    for (int i = 0; i < n; ++i)
        printf("%d\t", arr[i]);
    printf("\n");
}

void top_down(int *arr, int n) {
    for (int i = 1; i < n; ++i) {
        int child = i;
        while (child > 0) {
            int parent = (child - 1) / 2;
            if (arr[child] > arr[parent]) {
                swap(&arr[child], &arr[parent]);
                child = parent;
            } else {
                break;
            }
        }
    }
}

void heapsort(int *arr, int n) {
    if (n>1) {
        swap(&arr[0], &arr[n - 1]);
        n = n - 1;
        heapify(arr, n, 0);
        heapsort(arr, n);
    }
}

int main()
{
    int arr[] = {2, 9, 7, 6, 5, 8};
    int n = sizeof(arr) / sizeof(arr[0]);
    display(arr, n);
    // bottom_up(arr, n);
    top_down(arr, n);
    display(arr, n);
    heapsort(arr, n);
    display(arr, n);
    return 0;
}