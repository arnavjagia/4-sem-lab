/*
Write a program to find Minimum Cost Spanning Tree of a given undirected graph 
using Kruskal's algorithm and analyse its time efficiency.
*/

#include <stdio.h>
#include <stdlib.h>

// Structure to represent an edge in the graph
struct Edge {
    int src, dest, weight;
};

// Structure to represent a subset for union-find
struct Subset {
    int parent;
    int rank;
};

// Find operation of union-find with path compression
int find(struct Subset subsets[], int i) {
    if (subsets[i].parent != i)
        subsets[i].parent = find(subsets, subsets[i].parent);
    return subsets[i].parent;
}

// Union operation of union-find by rank
void unionSet(struct Subset subsets[], int x, int y) {
    int rootX = find(subsets, x);
    int rootY = find(subsets, y);

    if (subsets[rootX].rank < subsets[rootY].rank)
        subsets[rootX].parent = rootY;
    else if (subsets[rootX].rank > subsets[rootY].rank)
        subsets[rootY].parent = rootX;
    else {
        subsets[rootY].parent = rootX;
        subsets[rootX].rank++;
    }
}

// Comparator function for sorting edges by weight
int compare(const void* a, const void* b) {
    struct Edge* edgeA = (struct Edge*)a;
    struct Edge* edgeB = (struct Edge*)b;
    return edgeA->weight - edgeB->weight;
}

// Kruskal's algorithm to find Minimum Cost Spanning Tree
void kruskalMST(struct Edge edges[], int V, int E) {
    // Step 1: Sort edges by weight
    qsort(edges, E, sizeof(struct Edge), compare);

    // Allocate memory for subsets
    struct Subset* subsets = (struct Subset*)malloc(V * sizeof(struct Subset));

    // Initialize subsets
    for (int v = 0; v < V; v++) {
        subsets[v].parent = v;
        subsets[v].rank = 0;
    }

    int ecounter = 0; // Counter for edges in MST
    int i = 0; // Index variable for sorted edges

    // Array to store MST edges
    struct Edge resultMST[V - 1];

    // Step 2: Process edges in sorted order
    while (ecounter < V - 1 && i < E) {
        // Get the next edge from sorted list
        struct Edge nextEdge = edges[i++];

        int rootSrc = find(subsets, nextEdge.src);
        int rootDest = find(subsets, nextEdge.dest);

        // If including this edge doesn't cause a cycle, include it in the MST
        if (rootSrc != rootDest) {
            resultMST[ecounter++] = nextEdge;
            unionSet(subsets, rootSrc, rootDest);
        }
    }

    // Print the MST
    printf("Edges in the Minimum Cost Spanning Tree:\n");
    for (i = 0; i < V - 1; i++)
        printf("(%d, %d) -> %d\n", resultMST[i].src, resultMST[i].dest, resultMST[i].weight);

    free(subsets);
}

// Example usage
int main() {
    int V = 4; // Number of vertices
    int E = 5; // Number of edges

    // Graph edges with weights
    struct Edge edges[] = {
        {0, 1, 10},
        {0, 2, 6},
        {0, 3, 5},
        {1, 3, 15},
        {2, 3, 4}
    };

    // Apply Kruskal's algorithm
    kruskalMST(edges, V, E);

    return 0;
}

/* ---SAMPLE IO---
Edges in the Minimum Cost Spanning Tree:
(2, 3) -> 4
(0, 3) -> 5
(0, 1) -> 10
*/