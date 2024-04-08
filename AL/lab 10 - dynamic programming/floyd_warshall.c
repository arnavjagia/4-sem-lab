/*
Write a program to compute the transitive closure of a given directed graph using
Warshall’s algorithm and analyse its time efficiency. Obtain the experimental results
for order of growth and plot the result.
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct
{
    int **adj;
    int n;
} graph;

graph *init_graph()
{
    graph *temp = malloc(sizeof(*temp));
    printf("#vertices: ");
    scanf("%d", &temp->n);
    temp->adj = malloc(temp->n * sizeof(int *));
    for (int i = 0; i < temp->n; ++i)
    {
        temp->adj[i] = malloc(temp->n * sizeof(int));
        printf("Row %d: ", i);
        for (int j = 0; j < temp->n; ++j)
        {
            int value;
            scanf("%d", &value);
            temp->adj[i][j] = (value == -1) ? 999 : value;
        }
    }
    return temp;
}

graph warshall(graph g)
{
    for (int k = 0; k < g.n; ++k)
        for (int i = 0; i < g.n; ++i)
            for (int j = 0; j < g.n; ++j)
                g.adj[i][j] = g.adj[i][j] || (g.adj[i][k] && g.adj[k][j]);
    return g;
}

long int min(long int a, long int b) {
    return (a < b) ? a : b;
}

graph floyd(graph g) {
    for (int k = 0; k < g.n; ++k)
        for (int i = 0; i < g.n; ++i)
            for (int j = 0; j < g.n; ++j)
                g.adj[i][j] = min(g.adj[i][j], g.adj[i][k] + g.adj[k][j]);
    return g;
}

void display(graph *g)
{
    printf("\n---Graph---\n");
    for (int i = 0; i < g->n; ++i)
    {
        for (int j = 0; j < g->n; ++j)
        {
            printf("%d\t", g->adj[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    graph *g = init_graph();
    display(g);
    graph trans_closure = warshall(*g);
    graph shortest_dist_matrix = floyd(*g);
    display(&shortest_dist_matrix);
    display(&trans_closure);
    return 0;
}


/* --- SAMPLE IO ---
---Graph---
0       999     3       999
2       0       999     999
999     7       0       1
6       999     999     0

Floyd
---Graph---
0       10      3       4
2       0       5       6
7       7       0       1
6       16      9       0
*/