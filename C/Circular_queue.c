#include <stdio.h>
#include <stdlib.h>
#define N 10

int F=-1,R=-1;
void enqueue(int q[],int val)
{
	if((R+1)%N==F)
	{
		printf("\n Queue is full %d is not inserted",val);
	}
	else
	{
		R=(R+1)%N;
		q[R]=val;
		if(F==-1)
		{
			F=0;
		}
		
	}
}
int dequeue(int q[])
{
	int item;
	if(F==-1)
	{
		printf("\n Queue is empty");
		return 0;
	}
	item=q[F];
	if(F==R)
	{
		F=R=-1;
	}
	else
	{
		F=(F+1)%N;
	}
	return item;
}
void display(int q[])
{
	int i;
	for(i=F;i<=R;i++)
	{
		printf("\n The element is %d\n",q[i]);
	}	
	if(F==-1)
	{
		printf("\n There is no element");
	}

}
int main(int argc, char *argv[]) {
	int q[N];
	int val,n,item;
	printf("\n 1.Insert \t\n 2.Delete \t\n 3.Display \t\n 4.EXIT \t\n");
	do
	{
		printf("\nEnter choice = ");
	    scanf("%d",&n);
		switch(n)
		{
			case 1:
				printf("\nEnter the value of an element = ");
				scanf("%d",&val);
				enqueue(q,val);
				break;
			case 2:
				item = dequeue(q);
				if(item!=0) printf("\n%d is deleted",item);
				break;
			case 3:
				display(q);
				break;
			case 4:
				printf("EXIT");
		}
	}while(n!=4);
	return 0;
}

/* ""OUTPUT""

 1.Insert
 2.Delete
 3.Display
 4.EXIT

Enter choice = 1

Enter the value of an element = 10

Enter choice = 1

Enter the value of an element = 20

Enter choice = 1

Enter the value of an element = 30

Enter choice = 3

 The element is 10

 The element is 20

 The element is 30

Enter choice = 2

10 is deleted
Enter choice = 2

20 is deleted
Enter choice = 3

 The element is 30

Enter choice = 4
EXIT

*/
