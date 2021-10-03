#include<bits/stdc++.h>
using namespace std;
void sort_end (int profit[], int deadline[], int job[], int n)
{
	for (int i=0; i<n-1; i++)
	{
		int flag = 0;
		for (int j=0; j<n-1-i; j++)
		{
			if (profit[j] < profit[j+1])
			{
				swap(profit[j], profit[j+1]);
				swap(deadline[j], deadline[j+1]);
				swap(job[j], job[j+1]);
				flag = 1;
			}
		}
		if (flag == 0)
		break;
	}
//	for (int i=0; i<n; i++)
//	cout<<job[i]<<" ";
//	cout<<endl;
//	for (int i=0; i<n; i++)
//	cout<<profit[i]<<" ";
//	cout<<endl;
//	for (int i=0; i<n; i++)
//	cout<<deadline[i]<<" ";
//	cout<<endl;
}
void jobsSelected (int job[], int profit[], int deadline[], int n)
{
	int maxx = INT_MIN;
	int max_profit = 0;
	for (int i=0; i<n; i++)
	maxx = max(maxx, deadline[i]);
	int res[maxx]={0};
	for (int i=0; i<n; i++)
	{
		int x = deadline[i]-1;
		while (res[x] != 0 && x>=0)
		{
			x--;
		}
		if (x>=0 && x<n)
		{
			res[x] = job[i];
			max_profit += profit[i]; 
		}
	}
	for (int i=0; i<maxx; i++)
	{
		if (res[i] != 0)
		cout<<res[i]<<" ";
	}
	cout<<"\nMaximum profit is: "<<max_profit;
}
int main()
{
	int n;
	cout<<"\nEnter size of array: ";
	cin>>n;
	int job[n], profit[n], deadline[n];
	cout<<"\nEnter profit array: ";
	for (int i=0; i<n; i++)
	cin>>profit[i];
	cout<<"\nEnter deadline array: ";
	for (int i=0; i<n; i++)
	cin>>deadline[i];
	for (int i=0; i<n; i++)
	job[i] = i+1;
	sort_end(profit, deadline, job, n);
	cout<<"\nThe selected jobs are: ";
	jobsSelected(job, profit, deadline, n);
}
