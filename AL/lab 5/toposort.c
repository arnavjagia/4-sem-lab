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
    // printf("Visiting %d\n", v);
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
    stack *s = Stack(2 * V);
    int i;
    for(i = 0; i < V; ++i)
    {
        if(!visited[i]) {
            dfsv(i, s);
            push(s, i);
        }
        push(s, i);
    }

    printf("Toposort: ");
    for(i=V-1; i>=0; --i)
        printf("%d ", s->arr[i]);
    printf("\n");
}

void source_removal() {
    int *in_degree = calloc(V, sizeof(int));
    for(int i = 0; i < V; ++i) {
        for(int j = 0; j < V; ++j)
            in_degree[i] += g[j][i];
    }

    stack *s = Stack(V);
    for(int i = 0; i < V; ++i)
        if(in_degree[i] == 0)
            push(s, i);

    printf("Toposort: ");
    while(s->top != -1) {
        int v = s->arr[s->top--];
        printf("%d ", v);

        for(int i = 0; i < V; ++i) {
            if(g[v][i] != 0) {
                g[v][i] = 0;
                --in_degree[i];

                if(in_degree[i] == 0)
                    push(s, i);
            }
        }
    }
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
    source_removal();
    return 0;
}

/*
Enter the Number of Vertices: 
6
Enter the Adjacency Matrix: 
0 1 0 0 0 0 
0 0 1 1 0 0 
0 0 0 0 1 0 
0 0 0 0 1 1
0 0 0 0 0 1
0 0 0 0 0 0
Toposort: 0 1 3 2 4 5 
Toposort: 0 1 3 2 4 5 
*/
