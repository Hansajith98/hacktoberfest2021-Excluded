#include <iostream>  
using namespace std;  
int main()  
{  
	int num,rem,sum=0,temp;    
	cout<<"Enter the Number=  ";    
	cin>>num;    
	temp=num;    
	while(n>0)    
	{    
		rem=n%10;    
		sum=sum+(rem*rem*rem);    
		num=num/10;    
	}    
	if(temp==sum)    
	cout<<"Armstrong Number."<<endl;    
	else    
	cout<<"Not Armstrong Number."<<endl;   

}  
