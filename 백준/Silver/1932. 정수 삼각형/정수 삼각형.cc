#include <bits/stdc++.h>

using namespace std;

int n,temp;
int dp[1000][1000];
int v[1000][1000];

int dy(int num, int cur)
{
    if(num==n) return v[num][cur];
    if(dp[num][cur]!=0) return dp[num][cur];

    return dp[num][cur]=v[num][cur]+max(dy(num+1, cur), dy(num+1, cur+1));


}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin>>n;

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<=i; j++)
        {
            cin>>temp;
            v[i][j]=temp;
        }
    }
    cout<<dy(0, 0);

    return 0;
}
