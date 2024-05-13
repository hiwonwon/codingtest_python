#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

#define DIV 1000000000
int N;
vector<vector<int>> dp;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    dp = vector<vector<int>>(N+1,vector<int>(10,0));
    for(int i=0;i<10;i++) dp[1][i] = 1;
    dp[1][0] = 0;

    for(int i=2;i<=N;i++) {
        
        for(int j=0;j<10;j++) {

            if(j==0) {
                dp[i][1] += dp[i-1][0];
                dp[i][1] %= DIV;
            }
            else if(j == 9) {
                dp[i][8] += dp[i-1][9];
                dp[i][8] %= DIV;
            }
            else {
                dp[i][j-1] += dp[i-1][j];
                dp[i][j-1] %= DIV;
                dp[i][j+1] += dp[i-1][j];
                dp[i][j+1] %= DIV;
            }

        }

    }

    int ans = 0;
    for(int i=0;i<10;i++) {
        ans += dp[N][i];
        ans %= DIV;
    }
    cout << ans;
}

