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

typedef struct {
    int N;
    int **adj;
} graph;

typedef struct node {
    int val;
    struct node *next;
} node;

graph *Graph(int n_vertex) {
    graph *new = malloc(sizeof(graph));
    new->N = n_vertex;
    new->adj = malloc(N * sizeof(node*));
    for (int i = 0; i<N; ++i) {
        new->adj[i] = NULL;
    }
    return new;
}

int main() {
    stack *s = Stack(5);
    printf("%d\n", s->top);
    push(s, 1);
    printf("%d\n", s->arr[0]);
}
