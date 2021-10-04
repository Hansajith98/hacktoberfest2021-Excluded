// Program to return the index of the number which has the least distance with its neighbours
import java.util.Scanner;
import java.lang.Math;
class Least_Distance_Between_Neighbours
{
    static int smd(int[] ar)
    {
        int ind=0;
        int dist=Math.abs(ar[0]-ar[1]);
        for(int i=0;i<(ar.length-1);i++)
        {
            int val=Math.abs(ar[i]-ar[i+1]);
            if(val<dist)
            {
                dist=val;
                ind=i;
            }
        }
        return ind;
    }
    public static void main(String[] args)
    {
        int i;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of elements u want to enter");
        int n=sc.nextInt();
        int[] a=new int[n];
        for(i=0;i<n;i++)
        {
            System.out.println("Enter the number");
            a[i]=sc.nextInt();
        }
        int c=smd(a);
        System.out.println("The index is "+c);    
    }
}
