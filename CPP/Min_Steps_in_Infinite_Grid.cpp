#include <bits/stdc++.h>

using namespace std;

int coverPoints(vector<int> &A, vector<int> &B) {

	int n=A.size();
	int count=0;

	for (int i = 0; i < n-1; ++i)
	{
		
		if(abs(A[i]-A[i+1])<=abs(B[i]-B[i+1])){
			count+=abs(B[i]-B[i+1]);
		}else{
			count+=abs(A[i]-A[i+1]);

		}
	}

		return count;

	}



int main(){

	vector<int> A = {0, 1, 1};
 	vector<int>	B = {0, 1, 2};

 	cout<<coverPoints(A,B);


 	return 0;


}