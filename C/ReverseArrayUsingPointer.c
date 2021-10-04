#include<stdio.h>


void inputarr(int *ptr1,int n);
void printarr(int *ptr1,int n);
void reverse(int *ptr1,int *ptr2,int n);
int main()
{
    int arr1[20],arr2[20];
    int n=0;

    printf("\nEnter number of elements you want to insert\n");
    scanf("%d",&n);

//scanning array
    printf("\nEnter %d elements in array-1\n",n);
    inputarr(arr1,n);

//printing array b4 reversing
    printf("\nPrinting Elements of Array-1 \n\n");
    printarr(arr1,n);

//Reversing.

    reverse(arr1,&arr1[n-1],n);

    printf("\n\nArray after Reversing Elements \n \n");


    //printing array for before swap
    printf("\nPrinting Elements of Array-1 AFTER REVERSE \n\n");
    printarr(arr1,n);


    return 0;
}


void inputarr(int *ptr1,int n)
{

    for(int i=0; i<n; i++)
    {
        scanf("%d",ptr1);
        ptr1++;
    }

}

void printarr(int *ptr1,int n)
{

    for(int i=0; i<n; i++)
    {
        printf("| %d |",*ptr1);
        ptr1++;
    }

}


void reverse(int *ptr1,int *ptr2,int n)
{
    int temp;
    while(ptr1<ptr2)
    {
        temp=*ptr1;
        *ptr1=*ptr2;
        *ptr2=temp;
        ptr1++;
        ptr2--;

    }
}



