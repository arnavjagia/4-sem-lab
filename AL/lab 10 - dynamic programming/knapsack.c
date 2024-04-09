#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int knapsack(int W, int *wt, int *val, int n)
{
    int dp[n + 1][W + 1];

    for (int i = 0; i <= n; ++i)
        for (int w = 0; w <= W; ++w)
        {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            // item is available
            else if (w >= wt[i - 1])
                dp[i][w] = ((val[i - 1] + dp[i - 1][w - wt[i - 1]]) > dp[i - 1][w]) ? (val[i - 1] + dp[i - 1][w - wt[i - 1]]) : dp[i - 1][w];
            else
                dp[i][w] = dp[i - 1][w];
        }
    return dp[n][W];
}

int main()
{
    int w[] = {3, 1, 3, 4, 2};
    int v[] = {2, 2, 4, 5, 3};
    int W = 7;
    int n = sizeof(w) / sizeof(w[0]);
    printf("Max value is %d\n", knapsack(W, w, v, n));
    return 0;
}