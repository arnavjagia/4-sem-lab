#include <stdio.h>
#include <stdlib.h>


int iter = 0;


int *generate_sieve(int n) {
    int *is_prime = malloc((n + 1) * sizeof(int));


    is_prime[0] = is_prime[1] = 0;
    for (int i = 2; i < n; i++) {
        is_prime[i] = 1;
        iter += 1;
    }


    for (int i = 2; i <= n / 2; i++) {
        for (int j = 2; i * j <= n; j++) {
            is_prime[i * j] = 0;
            iter += 1;
        }
    }


    return is_prime;
}


int middle_school_gcd(int x, int y) {
    int n = x < y ? x : y;
    int *is_prime = generate_sieve(n); // size (n + 1)


    int gcd = 1;


    for (int i = 2; i <= x && i <= y; i++) {
        iter += 1;


        if (!is_prime[i])
            continue;
        
        if (x % i == 0 && y % i == 0) {
            x /= i;
            y /= i;
            gcd *= i;
            i -= 1; // perhaps i will divide x and y again
        }
    }


    return gcd;
}


int consecutive_integer_gcd(int x, int y) {
    int n = x < y ? x : y;


    for (int i = n; i > 1; i--) {
        iter += 1;
        if (x % i == 0 && y % i == 0)
            return i;
    }


    return 1;
}


int main() {
    while (1) {
        int x, y;
        printf("x: ");
        scanf("%d", &x);
        printf("y: ");
        scanf("%d", &y);


        iter = 0;
        printf("\nmiddle_school_gcd(%d, %d) = %d\n", x, y, middle_school_gcd(x, y));
        printf("n_iter = %d\n\n", iter);


        iter = 0;
        printf("consecutive_integer_gcd(%d, %d) = %d\n", x, y, consecutive_integer_gcd(x, y));
        printf("n_iter = %d\n\n", iter);
    }
}
