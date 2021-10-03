#include <bits/stdc++.h>
using namespace std;


int Partitions(int A,vector<int> &B){

	int ans=0;

	int total=0;
	std::vector<int> suffx(A,0);


	for (int i = 0; i <A; ++i)
	{

		total+=B[i];
	}

	if(total%3!=0){
		return ans;
	}

	long long part=total/3;
	long long local =0;

	for (int i = A-1; i >=0; i--)
	 {

	 		local+=B[i];

	 		if(local==part){
	 			suffx[i]=1;

	 		}
	 		
	 }

	 for (int i = A-2; i >=0; i--)
	  {
	  		
	  		suffx[i]+=suffx[i+1];

	  } 


	  local=0;

	  for (int i = 0; i+2 < A; ++i)
	  {
	  	local+=B[i];

	  	if(local==part){
	  		ans+=suffx[i+2];
	  	}
	  }

	  return ans;
}


int main(){

	std::vector<int> B={1, 2, 3, 0, 3};
	int A=5;


	cout<<Partitions(A,B)<<endl;
	




	return 0;

}