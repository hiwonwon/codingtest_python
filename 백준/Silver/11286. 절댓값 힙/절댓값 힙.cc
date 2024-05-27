#include <iostream>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    priority_queue<int, vector<int>, greater<int> > positive;
    priority_queue<int> negative;    
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        int t;
        cin >> t;
        if(!t && positive.empty() && negative.empty()) {
            cout << 0 << '\n';
        } else if(!t && !positive.empty() && negative.empty()) {
            cout << positive.top() << '\n';
            positive.pop();
        } else if(!t && positive.empty() && !negative.empty()) {
            cout << negative.top() << '\n';
            negative.pop();
        } else if(!t && !positive.empty() && !negative.empty()){
            if(abs(positive.top()) < abs(negative.top())) {
                cout << positive.top() << '\n';
                positive.pop();
            } else {
                cout << negative.top() << '\n';
                negative.pop();
            }
            
        } else if(t > 0){
            positive.push(t);
        } else if(t < 0) {
            negative.push(t);
        }
    } // for i
    return 0;
}