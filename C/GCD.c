#include <stdio.h>
int main()
{
	 int m, n;
	 printf("Enter 1st positive integers: ");
	 scanf("%d",&m);
	 printf("Enter 1st positive integers: ");
	 scanf("%d",&n);
	 while(n)
	 {
		  int tmp=n;
		  n=m%n;
		  m=tmp;
	 }
	 printf("GCD = %d",m);
	 return 0;
}
