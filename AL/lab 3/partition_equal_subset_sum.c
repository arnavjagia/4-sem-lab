/*
https://www.geeksforgeeks.org/problems/subset-sum-problem2014/1
https://leetcode.com/problems/partition-equal-subset-sum/description/
*/

#include <stdio.h>

int equalPartitionHelper(int arr[],int N, int index, int targetSum, int currentSum) {
    if (currentSum == targetSum)
        return 1;

    if (index == N || currentSum > targetSum)
        return 0;

    return equalPartitionHelper(arr,N, index + 1, targetSum, currentSum) ||
            equalPartitionHelper(arr,N, index + 1, targetSum, currentSum + arr[index]);
}

int equalPartition(int N, int arr[])
{ 
    int totalSum = 0;
    for (int i=0;i<N;i++)
        totalSum += arr[i];

    if (totalSum % 2 != 0)
        return 0;

    int targetSum = totalSum / 2;
    return equalPartitionHelper(arr,N, 0, targetSum, 0);
}


//{ Driver Code Starts.

int main(){
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int i = 0;i < N;i++)
        scanf("%d", &arr[i]);
    
    if(equalPartition(N, arr))
        printf("YES\n");
    else
        printf("NO\n");
    return 0;
}
// } Driver Code Ends
