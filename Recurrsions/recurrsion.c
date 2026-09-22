#include <stdio.h>
#include <stdio.h>

int calc(int n) {
    if (n <= 1) return 1;
    if (n % 2 == 0) return 2 * calc(n / 2);
    return calc(n - 1) + calc(n - 2);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Result: %d\n", calc(n));
    return 0;
}