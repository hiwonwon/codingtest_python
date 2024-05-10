// i번째 집에 어떤색이 들어올지 각각 따로 생각해서 점화식 만들기
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int money[1000][3];
vector<int> r;
vector<int> g;
vector<int> b;
int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int p1,p2,p3;
        cin>>p1>>p2>>p3;
        r.push_back(p1);
        g.push_back(p2);
        b.push_back(p3);
    }
    money[1][0] = r[0];
    money[1][1] = g[0];
    money[1][2] = b[0];
    for (int i = 2; i <= n; i++) {
        money[i][0] = min(money[i - 1][1], money[i - 1][2]) + r[i - 1];
        money[i][1] = min(money[i - 1][0], money[i - 1][2]) + g[i - 1];
        money[i][2] = min(money[i - 1][0], money[i - 1][1]) + b[i - 1];
    }
    int result = min({money[n][0],money[n][1],money[n][2]});
    /*
    int result1=min(money[n][0],money[n][1]);
    int result2=min(money[n][1],money[n][2]);
    int result3=min(result1,result2);
    */
    cout<<result;
}