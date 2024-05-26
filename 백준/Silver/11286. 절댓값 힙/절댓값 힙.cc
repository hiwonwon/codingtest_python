#include <iostream>
#include <queue>
#include <algorithm>
#include <cmath>

using namespace std;

struct cmp
{
    bool operator()(int a, int b)
    {
        if (abs(a) > abs(b))
        {
            return true;
        }
        else if (abs(a) == abs(b))
        {
            if (a > b)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        return false;
    }
};

priority_queue<int, vector<int>, cmp> myheap;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    while (N--)
    {
        int num;
        cin >> num;
        if (num == 0)
        {
            if (myheap.empty())
            {
                cout << '0' << '\n';
            }
            else
            {
                int temp = myheap.top();
                cout << temp << '\n';
                myheap.pop();
            }
        }
        else
        {
            myheap.push(num);
        }
    }
}