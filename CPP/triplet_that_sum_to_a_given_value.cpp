#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n,x;
        cin>>n;
        cin>>x;
        int A[n];
        for(int i=0;i<n;i++){
            cin>>A[i];
        }
        int ans=0;
        for(int i=0;i<n-2;i++){
            unordered_set<int>s;
            int sum=x-A[i];
            for(int j=i+1;j<n;j++){
                if(s.find(sum-A[i])!=s.end()){
                    ans=1;
                    break;
                }
                s.insert(A[j]);
            }
        }
        cout<<ans<<endl;
    }
}