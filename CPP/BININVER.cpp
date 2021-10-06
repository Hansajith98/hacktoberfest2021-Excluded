// Codechef Problem Odd GCD
//https://www.codechef.com/START14B/problems/BININVER/
#include<bits/stdc++.h>
using namespace std;
#define all(x) x.begin(), x.end()
#define ll long long
#define lld long double
#define lli long long int
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define INF 1e18
#define mod 1000000007
#include <string.h>

int main()
{
    FIO;
    ll t , a , b , n , m , k, i, j, cnt;
    cin>>t;
    string s , st;
    while(t--){
        cin>>n;
        vector<ll> v(n);
        ll eve = 0;
        for(i=0;i<n;i++){
            cin>>v[i];
            if(!(v[i]&1)){
                eve++;
            }
        }
        if(eve==n){
        ll ans = 1e9;
        for(i=0;i<n;i++){
                cnt = 0;
                while(!(v[i]&1)){
                    v[i]/=2;
                    cnt++;
                }
                ans = min(cnt,ans);
        }
        cout<<ans<<endl;
        }
        else{
                cout<<0<<endl;
        }

    }

    return 0;
}
