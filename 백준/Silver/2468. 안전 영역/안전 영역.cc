#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

typedef long long ll;

int n, a[100][100];
int bottom = 1e9, top = 0, ans = 1;
bool graph[100][100], visited[100][100];

int x_dir[4] = { -1, 1, 0, 0 };
int y_dir[4] = { 0, 0, -1, 1 };

struct coord {
  int x, y;
};

void bfs(coord start) {
  queue<coord> q;
  q.push(start);
  visited[start.x][start.y] = true;

  while(!q.empty()) {
    coord cur = q.front();
    q.pop();

    for(int i = 0; i < 4; i++) {
      int x = cur.x + x_dir[i];
      int y = cur.y + y_dir[i];
      
      if(x < 0 || x >= n || y < 0 || y >= n) continue;

      if(graph[x][y] && !visited[x][y]) {
        q.push({ x, y });
        visited[x][y] = true;
      }

    }
  }

}

void init(int h) {
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
        graph[i][j] = a[i][j] > h;
        visited[i][j] = false;
    }
  }
}

int main() {
  cin >> n;

  for(int i = 0; i < n; i++) {
    for(int j = 0; j < n; j++) {
      cin >> a[i][j];
      bottom = min(bottom, a[i][j]);
      top = max(top, a[i][j]);
    }
  }

  for(int h = bottom; h < top; h++) {
    init(h);
    int cnt = 0;
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        if(graph[i][j] && !visited[i][j]) {
          cnt++;
          bfs({ i, j });
        }
      }
    }

    ans = max(ans, cnt);
  }

  cout << ans; 
  return 0;
}

