#include<bits/stdc++.h>
#include<cmath>
using namespace std;
int lcs(string a, string b, int m, int n)
{
    int dp[m+1][n+1];
    for(int i=0; i<=m; i++)
        dp[i][0] = 0;
    for(int i=0; i<=n; i++)
        dp[0][i] = 0;
    for(int i=1; i<=m; i++)
    {
        for(int j=1; j<=n; j++)
        {
            if(a[i-1] == b[j-1])
            {
                dp[i][j] = 1+ dp[i-1][j-1];
            }
            else
            {
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[m][n];
}
int main()
{
    string a, b;
    int m, n;
    cin>>a;
    cin>>b;
    m = a.length();
    n = b.length();
    cout<<lcs(a, b, m, n);
    return 0;
}