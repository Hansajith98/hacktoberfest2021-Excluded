#include <bits/stdc++.h>
using namespace std;


int maxArr(vector<int> &a){

	int max1=INT_MIN,min1=INT_MAX,max2=INT_MIN,min2=INT_MAX;


	for (int i = 0; i <a.size(); ++i)
	{
		
		max1=max(max1,a[i]+i);
        min1=min(min1,a[i]+i);
        max2=max(max2,a[i]-i);
        min2=min(min2,a[i]-i);

	}

	int ans=INT_MIN;

	for (int i = 0; i <a.size(); ++i)
	{

		ans=max(ans,abs(a[i]+i));
		ans=max(ans,abs(a[i]+i));
		ans=max(ans,abs(a[i]-i));
		ans=max(ans,abs(a[i]-i));
		
	}


	return ans;

}

int main(){

	vector<int> a={1, 3, -1};

	cout<<maxArr(a)<<endl;



}