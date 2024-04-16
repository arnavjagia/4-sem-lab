/*
Given a weighted connected graph, write a program to implement Dijkstra’s algorithm
to find the shortest path from a given vertex to other vertices in the graph. Also, analyze
the time efficiency of the algorithm
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define V 5 // Number of vertices in the graph

// Function to find the vertex with the minimum distance value,
// from the set of vertices not yet included in the shortest path tree
int minDistance(int dist[], int visited[])
{
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++)
    {
        if (visited[v] == 0 && dist[v] <= min)
        {
            min = dist[v];
            min_index = v;
        }
    }

    return min_index;
}

// Function to print the shortest path from the source to the given vertex
void printSolution(int dist[], int parent[], int src)
{
    printf("Vertex\t Distance\t Path\n");
    for (int i = 0; i < V; i++)
    {
        printf("%d -> %d\t %d\t\t", src, i, dist[i]);

        // Track the path from the destination vertex back to the source
        int pathStack[V]; // Stack to store the reversed path
        int pathLength = 0;
        int j = i;

        // Build the path stack by backtracking from the destination to the source
        while (j != -1)
        {
            pathStack[pathLength++] = j;
            j = parent[j];
        }

        // Print the path by popping elements from the stack (reversed order)
        for (int k = pathLength - 1; k >= 0; k--)
        {
            printf("%d", pathStack[k]);
            if (k > 0)
                printf(" -> ");
        }
        printf("\n");
    }
}


// Dijkstra's algorithm implementation
void dijkstra(int graph[V][V], int src)
{
    int dist[V];    // The output array dist[i] holds the shortest distance from src to i
    int visited[V]; // visited[i] will be true if vertex i is included in the shortest path tree
    int parent[V];  // parent[i] will store the parent node in the shortest path from src to i

    // Initialize all distances as INFINITE and visited[] as false
    for (int i = 0; i < V; i++)
    {
        dist[i] = INT_MAX;
        visited[i] = 0;
        parent[i] = -1;
    }

    // Distance of source vertex from itself is always 0
    dist[src] = 0;

    // Find shortest path for all vertices
    for (int count = 0; count < V - 1; count++)
    {
        // Pick the minimum distance vertex from the set of vertices not yet processed
        int u = minDistance(dist, visited);

        // Mark the picked vertex as visited
        visited[u] = 1;

        // Update dist value of the adjacent vertices of the picked vertex
        for (int v = 0; v < V; v++)
        {
            // Update dist[v] only if it's not visited, there's an edge from u to v,
            // and the total weight of path from src to v through u is less than current value of dist[v]
            if (!visited[v] && graph[u][v] && dist[u] != INT_MAX && dist[u] + graph[u][v] < dist[v])
            {
                dist[v] = dist[u] + graph[u][v];
                parent[v] = u;
            }
        }
    }

    // Print the constructed distance array
    printSolution(dist, parent, src);
}

// Example usage
int main()
{
    // Example weighted graph adjacency matrix
    int graph[V][V] = {
        {0, 3, 0, 7, 0},
        {3, 0, 4, 2, 0},
        {0, 4, 0, 5, 6},
        {7, 2, 5, 0, 4},
        {0, 0, 6, 4, 0}
    };
    // int graph[V][V] = {
    //     {0, 4, 0, 0, 0, 0},
    //     {4, 0, 8, 0, 0, 0},
    //     {0, 8, 0, 7, 0, 4},
    //     {0, 0, 7, 0, 9, 14},
    //     {0, 0, 0, 9, 0, 10},
    //     {0, 0, 4, 14, 10, 0}
    // };

    int source = 0; // Source vertex (starting point for Dijkstra's algorithm)

    printf("Shortest Paths from vertex %d:\n", source);
    dijkstra(graph, source);

    return 0;
}

/*---SAMPLE IO---
Shortest Paths from vertex 0:
Vertex   Distance        Path
0 -> 0   0              0
0 -> 1   3              0 -> 1
0 -> 2   7              0 -> 1 -> 2
0 -> 3   5              0 -> 1 -> 3
0 -> 4   9              0 -> 1 -> 3 -> 4
*/