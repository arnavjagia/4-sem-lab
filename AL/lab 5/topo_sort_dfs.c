/*
Write a program to determine the Topological sort of a given graph using
i. Depth-First technique
ii. Source removal technique

https://github.com/my-lambda-projects
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *arr;
    int top;
} stack;

stack *Stack(int size) {
    stack *new = malloc(sizeof(stack));
    new->arr = malloc(size * sizeof(int));
    new->top = -1;
    return new;
}

void push(stack *s, int vertex) {
    s->arr[++s->top] = vertex;
}

int g[10][10];
int V;
int visited[10];

void dfsv(int v, stack *s)
{
    printf("Visiting %d\n", v);
    visited[v] = 1;
    int i;
    for(i = 0; i < V; ++i)
    {
        if(!(visited[i]) && (g[v][i] == 1) && (i != v)) {
            dfsv(i, s);
            push(s, i);
        }
    }
}

void dfs_sort()
{
    stack *s = Stack(V);
    int i;
    for(i = 0; i < V; ++i)
    {
        if(!visited[i]) {
            dfsv(i, s);
            push(s, i);
        }
        push(s, i);
    }

    for(i=V-1; i>=0; --i)
        printf("%d ", s->arr[i]);
    printf("\n");
}

int main()
{
    printf("Enter the Number of Vertices: \n");
    scanf("%d", &V);
    int i, j;
    printf("Enter the Adjacency Matrix: \n");
    for(i = 0; i < V; ++i)
    {
        for(j = 0; j < V; ++j)
        scanf(" %d", &g[i][j]);
    }
    dfs_sort();
    return 0;
}
