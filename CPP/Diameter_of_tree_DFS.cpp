#include <bits/stdc++.h>
using namespace std;

int visited[10001];
vector<int> edge[10001];
int dis[10001];

void dfs(int node, int distance)
{
    visited[node]=1;
    dis[node]=distance;

    for(int child:edge[node])
    {
        if(visited[child]==0)
        {
            dfs(child,distance+1);
        }
    }
}


int main()
{
    
        int n,e; // n is number of node, e is number of edges

        cin>>n>>e;

        while(e--)
        {
            int a,b;
            cin>>a>>b;
            edge[a].push_back(b);
            edge[b].push_back(a);
        }
        
        dfs(1,0);

        int maxd = -1; // maximum distance of node from root
        int maxi =-1; // node whose distance is maximum


        for(int i=1;i<=n;i++)
        {
            if(dis[i]>maxd)
            {
                maxd = dis[i];
                maxi = i;
            }
        }

        for(int i=0;i<=n;i++)
        {
            dis[i]=0;
            visited[i]=0;
        }



        dfs(maxi,0);

        int ansd = -1; 
        int ansi = -1;

        for(int i=1;i<=n;i++)
        {
            if(dis[i]>ansd)
            {
                ansd = dis[i];
                ansi = i;
            }
        }
        cout<<ansd<<endl;

}
