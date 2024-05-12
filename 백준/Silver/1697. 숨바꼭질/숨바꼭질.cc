#include <bits/stdc++.h>
using namespace std;

int n,m;
int p[100005];
int vis[100005];
queue<int> q;

int dx[3]={1,1,2};
int dy[3]= {1,-1,0};


int main(){
    cin >> n>> m;
    
    vis[n]=1;
    q.push(n);
    
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        
        
        for(int k=0;k<3;k++){
            int ncur = dx[k]*cur+dy[k];
            if(ncur>=0 && ncur <=100000 && vis[ncur]==0){
                q.push(ncur);
                vis[ncur]=1;
                p[ncur]=p[cur]+1;
            }
        }
    }
    
    cout << p[m];
}