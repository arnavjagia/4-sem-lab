/*
Write a C program to find the solution to the subset-sum problem using backtracking.
Consider the test case S={1, 2, 5, 6, 8} and d=9, to verify your answer.
*/

#include <stdio.h>

#define MAX_SIZE 100

// Function to recursively find subset with given sum using backtracking
int isSubsetSum(int set[], int n, int sum, int targetSum, int index, int currentSum) {
    // Base case: if current sum is equal to target sum
    if (currentSum == targetSum) {
        printf("Subset with sum %d found: ", targetSum);
        for (int i = 0; i < index; i++) {
            printf("%d ", set[i]);
        }
        printf("\n");
        return 1; // Solution found
    }

    // Base case: if all elements are processed
    if (index == n) {
        return 0; // No subset with the target sum found
    }

    // Include the current element in the subset (if it does not exceed the target sum)
    if (currentSum + set[index] <= targetSum) {
        // Recursively try including the current element in the subset
        if (isSubsetSum(set, n, sum, targetSum, index + 1, currentSum + set[index])) {
            return 1; // Solution found
        }
    }

    // Exclude the current element from the subset
    return isSubsetSum(set, n, sum, targetSum, index + 1, currentSum);
}

// Function to solve subset-sum problem using backtracking
void subsetSum(int set[], int n, int targetSum) {
    int sum = 0; // Calculate sum of all elements in the set
    for (int i = 0; i < n; i++) {
        sum += set[i];
    }

    // If total sum is less than target sum, no solution possible
    if (sum < targetSum) {
        printf("No subset with sum %d found.\n", targetSum);
        return;
    }

    // Use recursive backtracking to find the subset with the target sum
    if (!isSubsetSum(set, n, sum, targetSum, 0, 0)) {
        printf("No subset with sum %d found.\n", targetSum);
    }
}

// Main function to test the subset-sum problem
int main() {
    int set[] = {1, 2, 5, 6, 8};
    int n = sizeof(set) / sizeof(set[0]);
    int targetSum = 9;

    printf("Finding subset with sum %d in set {1, 2, 5, 6, 8}:\n", targetSum);
    subsetSum(set, n, targetSum);

    return 0;
}


/*---SAMPLE IO---
Finding subset with sum 9 in set {1, 2, 5, 6, 8}:
Subset with sum 9 found: 1 2 5 6
*/