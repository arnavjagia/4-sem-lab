/*
Write a program to find GCD using middle school method and analyze its time efficiency.
*/

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

int main() {
      int x, y;
      printf("Enter a and b: ");
      scanf("%d %d", &x, &y);

      iter = 0;
      printf("\nmiddle_school_gcd(%d, %d) = %d\n", x, y, middle_school_gcd(x, y));
      printf("n_iter = %d\n\n", iter);
}

/*
Enter a and b: 12 18

middle_school_gcd(12, 18) = 6
n_iter = 25

consecutive_integer_gcd(12, 18) = 6
n_iter = 7

Enter a and b: 45 60

middle_school_gcd(45, 60) = 15
n_iter = 141

consecutive_integer_gcd(45, 60) = 15
n_iter = 31

Enter a and b: 101 103

middle_school_gcd(101, 103) = 1
n_iter = 482

consecutive_integer_gcd(101, 103) = 1
n_iter = 100

Enter a and b: 56 72

middle_school_gcd(56, 72) = 8
n_iter = 191

consecutive_integer_gcd(56, 72) = 8
n_iter = 49

Enter a and b: 81 27

middle_school_gcd(81, 27) = 27
n_iter = 71

consecutive_integer_gcd(81, 27) = 27
n_iter = 1

Enter a and b: 35 49

middle_school_gcd(35, 49) = 7
n_iter = 101

consecutive_integer_gcd(35, 49) = 7
n_iter = 29

Enter a and b: 24 36

middle_school_gcd(24, 36) = 12
n_iter = 63

consecutive_integer_gcd(24, 36) = 12
n_iter = 13

Enter a and b: 66 99

middle_school_gcd(66, 99) = 33
n_iter = 236

consecutive_integer_gcd(66, 99) = 33
n_iter = 34

Enter a and b: 100 200

middle_school_gcd(100, 200) = 100
n_iter = 388

consecutive_integer_gcd(100, 200) = 100
n_iter = 1

Enter a and b: 88 176

middle_school_gcd(88, 176) = 88
n_iter = 335

consecutive_integer_gcd(88, 176) = 88
n_iter = 1
*/
