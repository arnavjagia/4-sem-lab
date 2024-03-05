/*
Write a program to create a heap for the list of integers using top-down heap
construction algorithm and analyze its time efficiency. Obtain the experimental
results for order of growth and plot the result.
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 1000

int count = 0;

typedef struct {
    int array[MAX_SIZE];
    int n;
} *heap;

void display_array(int *a, int n) {
    // Display `n` elements of the array `a`
    for (int i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

heap new_heap() {
    heap h = malloc(sizeof(*h));
    h->n = 0;
    return h;
}

void insert(heap h, int x) {
    if (h->n == MAX_SIZE) {
        printf("Heap full\n");
        return;
    }
    h->n++;
    h->array[h->n] = x;
    
    int i = h->n;
    int parent = i / 2;
    
    while (parent > 0 && h->array[parent] > h->array[i]) {
        count++;
        swap(h->array + parent, h->array + i);
        i = parent;
        parent = i / 2;
    }
}

int main() {
    heap h = new_heap();
    printf("Enter heap elements, -1 to stop: ");
    while (1) {
        int x; 
        scanf("%d", &x);
        if (x == -1) break;
        insert(h, x);
    }
    printf("Heap: ");
    display_array(h->array + 1, h->n);
    printf("\nopcount: %d", count);
}

/* ---SAMPLE IO---
Enter heap elements, -1 to stop: 2 3 1 5 4 -1
Heap: 1 3 2 5 4 

opcount: 1
*/
