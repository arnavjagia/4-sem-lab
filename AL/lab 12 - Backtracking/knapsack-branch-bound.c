/*
Write a C program to implement Knapsack problem using branch and bound 
technique.
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_ITEMS 100

// Structure to represent an item
struct Item {
    int weight;
    int value;
};

// Priority queue (min-heap) implementation for nodes
struct PriorityQueue {
    int size;
    int capacity;
    struct Node* array;
};

// Comparator function for qsort to compare items based on value/weight ratio
int compareItems(const void* a, const void* b) {
    const struct Item* itemA = (const struct Item*)a;
    const struct Item* itemB = (const struct Item*)b;
    double ratioA = (double)itemA->value / itemA->weight;
    double ratioB = (double)itemB->value / itemB->weight;
    if (ratioA < ratioB) return 1;   // Sort in descending order based on value/weight ratio
    if (ratioA > ratioB) return -1;
    return 0;
}

// Function to initialize priority queue
struct PriorityQueue* createPriorityQueue(int capacity);

// Function to solve knapsack problem using branch and bound
int knapsackBranchBound(int capacity, struct Item items[], int n);

// Main function to test knapsack problem using branch and bound
int main() {
    struct Item items[] = {{3, 40}, {5, 70}, {6, 30}, {7, 80}};
    int capacity = 15;
    int n = sizeof(items) / sizeof(items[0]);

    int maxProfit = knapsackBranchBound(capacity, items, n);
    printf("Maximum value achievable: %d\n", maxProfit);

    return 0;
}

// Function definitions

// Structure for priority queue (min-heap) node
struct Node {
    int level;
    int value;
    int weight;
    int bound;
};

// Function to swap two nodes in the priority queue
void swapNodes(struct Node* a, struct Node* b) {
    struct Node temp = *a;
    *a = *b;
    *b = temp;
}

// Function to initialize priority queue
struct PriorityQueue* createPriorityQueue(int capacity) {
    struct PriorityQueue* pq = (struct PriorityQueue*)malloc(sizeof(struct PriorityQueue));
    pq->size = 0;
    pq->capacity = capacity;
    pq->array = (struct Node*)malloc((size_t)pq->capacity * sizeof(struct Node));
    return pq;
}

// Function to insert a node into priority queue
void insertNode(struct PriorityQueue* pq, struct Node node) {
    if (pq->size == pq->capacity) {
        printf("Priority queue is full!\n");
        return;
    }
    pq->array[pq->size] = node;
    pq->size++;
}

// Function to extract minimum value node from priority queue
struct Node extractMin(struct PriorityQueue* pq) {
    struct Node minNode = pq->array[0];
    pq->array[0] = pq->array[pq->size - 1];
    pq->size--;
    // Re-heapify to maintain heap property
    int i = 0;
    while (1) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int smallest = i;
        if (left < pq->size && pq->array[left].bound < pq->array[smallest].bound)
            smallest = left;
        if (right < pq->size && pq->array[right].bound < pq->array[smallest].bound)
            smallest = right;
        if (smallest != i) {
            swapNodes(&pq->array[i], &pq->array[smallest]);
            i = smallest;
        } else {
            break;
        }
    }
    return minNode;
}

// Function to calculate upper bound of a node
int calculateBound(struct Node u, int n, int capacity, struct Item items[]) {
    if (u.weight >= capacity)
        return 0;

    int totalValue = u.value;
    int totalWeight = u.weight;
    int j = u.level + 1;

    while (j < n && totalWeight + items[j].weight <= capacity) {
        totalWeight += items[j].weight;
        totalValue += items[j].value;
        j++;
    }

    if (j < n)
        totalValue += (capacity - totalWeight) * items[j].value / items[j].weight;

    return totalValue;
}

// Function to solve knapsack problem using branch and bound
int knapsackBranchBound(int capacity, struct Item items[], int n) {
    // Sort items based on value/weight ratio (descending order)
    qsort(items, n, sizeof(struct Item), (int (*)(const void *, const void *))compareItems);

    struct PriorityQueue* pq = createPriorityQueue(MAX_ITEMS);

    struct Node u, v;
    u.level = -1;
    u.value = u.weight = 0;
    u.bound = calculateBound(u, n, capacity, items);

    int maxProfit = 0;
    insertNode(pq, u);

    while (pq->size) {
        u = extractMin(pq);

        if (u.bound > maxProfit) {
            v.level = u.level + 1;
            v.weight = u.weight + items[v.level].weight;
            v.value = u.value + items[v.level].value;

            if (v.weight <= capacity && v.value > maxProfit)
                maxProfit = v.value;

            v.bound = calculateBound(v, n, capacity, items);

            if (v.bound > maxProfit)
                insertNode(pq, v);

            v.weight = u.weight;
            v.value = u.value;
            v.bound = calculateBound(v, n, capacity, items);

            if (v.bound > maxProfit)
                insertNode(pq, v);
        }
    }

    return maxProfit;
}
