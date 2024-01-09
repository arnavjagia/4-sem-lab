/*
Write a program to implement the following graph representations and display
them.
i. Adjacency list
ii. Adjacency matrix
*/

#include <stdio.h>
#include <stdlib.h>

// Define the Node structure
typedef struct Node {
    int value;
    struct Node *next;
    struct Node *prev;
} *Node;

// Function to search a node in the list
int search(Node n, int value) {
    if (!n) return 0;
    if (n->value == value) return 1;

    for (Node walk = n->next; walk != n; walk = walk->next) {
        if (walk->value == value) return 1;
    }

    return 0;
}

// Function to insert a node in the list
void insert(Node *root, int value) {
    if (search(*root, value)) {
        printf("Edge already exists\n");
        return;
    }

    Node new_node = malloc(sizeof(*new_node));
    new_node->value = value;

    if (!*root) {
        *root = new_node;
        new_node->prev = new_node->next = new_node;
        return;
    }

    new_node->prev = (*root)->prev;
    new_node->prev->next = new_node;
    new_node->next = *root;
    (*root)->prev = new_node;
}

// Function to display the adjacency list
void display_adj_list(Node *adj_list, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d --> ", i);
        
        if (adj_list[i]) {
            printf("%d ", adj_list[i]->value);
            for (Node walk = adj_list[i]->next; walk != adj_list[i]; walk = walk->next)
                printf("%d ", walk->value);
            printf("\n");
        }
    }
}

// Function to display the adjacency matrix
void display_adj_matrix(Node *adj_list, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) 
            if (search(adj_list[i], j)) 
                printf("1 ");
            else
                printf("0 ");
        printf("\n");
    }
}

// Main function
int main() {
    int n;
    printf("How many nodes: ");
    scanf("%d", &n);
    Node *adj_list = malloc(n * sizeof(*adj_list));

    for (int i = 0; i < n; i++) 
        adj_list[i] = NULL;

    printf("\nEnter edges, enter -1 to end input\n\n");
    while (1) {
        int start, end;
        printf("From: ");
        scanf("%d", &start);
        printf("To: ");
        scanf("%d", &end);

        if (start == -1 | end == -1)
            break;

        insert(&(adj_list[start]), end);
        printf("Edge addition complete\n\n");
    }

    printf("\n\nAdjacency list: \n");
    display_adj_list(adj_list, n);
    
    printf("\n\nAdjacency matrix: \n");
    display_adj_matrix(adj_list, n);

    printf("\n");
}

/*
How many nodes: 3

Enter edges, enter -1 to end input

From: 0
To: 0
Edge addition complete

From: 1
To: 1
Edge addition complete

From: 2
To: 2
Edge addition complete

From: 2
To: 0
Edge addition complete

From: -1
To: -1


Adjacency list: 
0 --> 0 
1 --> 1 
2 --> 2 0 


Adjacency matrix: 
1 0 0 
0 1 0 
1 0 1 
*/
