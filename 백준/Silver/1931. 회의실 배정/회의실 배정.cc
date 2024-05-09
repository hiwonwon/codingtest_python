#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

typedef pair <int, int> pii;

vector<pii> meeting;
int n;

void input()
{
    int st, fin;
    cin >> n;
    for(int i=0; i < n; i++)
    {
        cin >> st >> fin;
        meeting.push_back(pii(st, fin));
    }
}

bool cmp(pii a, pii b)
{
    if(a.second < b.second)return 1;
    else if(a.second > b.second)return 0;
    else if(a.first < b.first)return 1;
    else return 0;
}

int greedy(int time, int num, int cnt)
{
    for(int i = num; i < n; i++)
        if(meeting[i].first >= time)return greedy(meeting[i].second, i+1, cnt+1);

    return cnt;
}

int main()
{
    input();

    sort(meeting.begin(), meeting.end(), cmp);

    cout << greedy(0, 0, 0);

    return 0;
}
