#include <stdio.h>
/* Include other headers as needed */
int main()
{
  int num,l,n,i,j,a[100][100],b[100][100],k;
  scanf("%d",&num);
   for(l=1;l<=num;l++)
   {
      scanf("%d",&n);
     for(i=0;i<n;i++)
     {
       for(j=0;j<n;j++)
       {
          scanf("%d",&a[i][j]);    
       }
     }
   for(i=0;i<n;i++)
   {
     for(j=0;j<n;j++)
     {
       b[i][j]=a[j][i];  
     }
   }
    
     for(i=0;i<n;i++)
     {
        k=n-1;
       for(j=0;j<n;j++)
       {
         a[i][k]=b[i][j];
         k--;
       } 
     }
     
     for(i=0;i<n;i++)
     {
       for(j=0;j<n;j++)
       {
         printf("%d",a[i][j]);
         if(j<n-1)
           printf(" ");
       }
       printf("\n");
     }
     printf("\n");
   }

    return 0;

}
