#include <stdio.h>
int main()
{
    // name - Ranjan kumar
    // github name - ranjan1560
    // github profile link - https://github.com/ranjan1560

    
	int a;
	printf("Enter amount of multiple 5:");
	scanf("%d",&a);
	printf("No. of 2000 note %d",a/2000);
	a=a%2000;
	printf("\nNo. of 1000 note %d",a/1000);
	a=a%1000;
	printf("\nNo. of 500 note %d",a/500);
	a=a%500;
	printf("\nNo. of 200 note %d",a/200);
	a=a%200;
	printf("\nNo. of 100 note %d",a/100);
	a=a%100;
	printf("\nNo. of 50 note %d",a/50);
	a=a%50;
	printf("\nNo. of 20 note %d",a/20);
	a=a%20;
	printf("\nNo. of 10 note %d",a/10);
	a=a%10;
	printf("\nNo. of 5 note %d",a/5);
}