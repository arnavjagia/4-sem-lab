#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int vertex;
    struct node* next;
} node;

typedef struct Graph {
    int numVertices;
    node** adjLists;
} Graph;

node* createNode(int v) {
    node* newNode = malloc(sizeof(node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

Graph* createGraph(int vertices) {
    Graph* graph = malloc(sizeof(Graph));
    graph->numVertices = vertices;

    graph->adjLists = malloc(vertices * sizeof(node*));

    int i;
    for (i = 0; i < vertices; i++)
        graph->adjLists[i] = NULL;

    return graph;
}

void addEdge(Graph* graph, int src, int dest) {
    // Add edge from src to dest
    node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;

    // Add edge from dest to src
    newNode = createNode(src);
    newNode->next = graph->adjLists[dest];
    graph->adjLists[dest] = newNode;
}

void printGraph(Graph* graph) {
    int v;
    for (v = 0; v < graph->numVertices; v++) {
        node* temp = graph->adjLists[v];
        printf("\n Adjacency list of vertex %d\n ", v);
        while (temp) {
            printf("%d -> ", temp->vertex);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    Graph* graph = createGraph(5);
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 4);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 1, 4);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 4);

    printGraph(graph);

    return 0;
}
