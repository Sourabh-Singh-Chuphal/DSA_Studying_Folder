#include <stdio.h>
void greet()
{
    printf("Hello, welcome!\n");
}
int add(int a, int b){
    return a + b;
}
int main() {
    int var = 22;

    printf("var = %d \n", var);
    
    char ch = 'A';
    
    printf("ch = %c \n", ch);
    greet();

    int arr[5] = {10, 20, 30, 40, 50};

    printf("First element: %d\n", arr[0]);
    printf("Third element: %d\n", arr[2]);

    int x = 10;
    int *ptr = &x;

    printf("Value of x: %d\n", x);
    printf("Address of x: %p\n", (void *)&x);
    printf("Value using pointer: %d\n", *ptr);

    printf("Sum of 5 and 10 is: %d\n", add(5, 10));

    return 0;
}




    
