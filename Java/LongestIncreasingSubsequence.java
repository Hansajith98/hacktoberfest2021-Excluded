"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

import java.util.*;

class Solution {

    public static int lengthOfLIS(int[] a) {
        int dp[]=new int[a.length+1];
        Arrays.fill(dp,1);
        for(int i=1;i<=a.length;i++){
            int max=0;
            for(int j=1;j<i;j++){
                if(a[j-1]<a[i-1]){
                    max=Math.max(max,dp[j]);
                }
            }
            dp[i]=max+1;
        }
        int ans=0;
        for(int i:dp)
            ans=Math.max(ans,i);
        return ans;
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of array :- ");
        int a=sc.nextInt();
        int arr[]=new int[a];
        System.out.println("Enter the elements of array :- ");
        for(int i=0;i<a;i++){
            arr[i]=sc.nextInt();
        }
        System.out.println("The maximum array size with increasing subsequence is :- "+lengthOfLIS(arr));
    }
}