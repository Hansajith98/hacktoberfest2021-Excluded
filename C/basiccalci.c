#include <stdio.h>
int main()
{
    char operator;
    int a, b;
    printf("Enter the number a, b: \n");
    scanf("%d %d", &a, &b);
    printf("Enter the operator: \n");
    scanf(" %c", &operator);
    switch (operator)
    {
    case '+':
        printf("%d + %d = %d", a, b, a + b);
        break;
    case '-':
        printf("%d - %d = %d", a, b, a - b);
        break;
    case '*':
        printf("%d * %d = %d", a, b, a * b);
        break;
    case '/':
        printf("%d / %d = %d", a, b, a / b);
        break;
    case '%':
        printf("%d %% %d = %d", a, b, a % b);
        break;
    default:
        printf("You have given an invalid operator.");
    }
    return 0;
}
