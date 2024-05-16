 #include <cstdio>
#include <queue>
#include <algorithm>

struct cmp{
    bool operator()(int& a, int& b){
        if(std::abs(a)==std::abs(b)){
            return a>b;
        }
        return abs(a)>abs(b);
    }
};

int main(int argc, char * argv[]){
    std::priority_queue<int, std::vector<int>, cmp> q;

    int n;

    int x;
    int i;

    scanf("%d", &n);

    for(i=0; i<n; i++){
        scanf("%d", &x);
        if(x) q.push(x);
        else{
            if(q.size()){
                printf("%d\n", q.top());
                q.pop();
            }else{
                printf("0\n");
            }
        }
    }
    return 0;
}