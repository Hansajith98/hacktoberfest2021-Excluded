/* Given two integers x and n, write a function to compute xn. 
We may assume that x and n are small and overflow doesn’t happen.*/
#include<stdio.h>

float powerOfX(float x, int y) {
	float tempVar;
	if(y == 0) return 1;
	tempVar = powerOfX(x, y/2);	
	
	if(y%2 == 0) return tempVar*tempVar;
	else {
		if(y > 0) return x*tempVar*tempVar;
		else return (tempVar*tempVar)/x;
	}
}

int main() {
	float x;
	scanf("%f",&x);
	int n ;
	scanf("%d",&n);
	printf("%.2f", powerOfX(x, n));
	return 0;
}