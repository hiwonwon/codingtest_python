#include <iostream>
#include <queue>
#include <string>

using namespace std;

#define X first
#define Y second

int N, M;
string maze[101];
bool visit[101][102];
int Time[101][102];
int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

queue<pair<int, int>> myQueue;

int main(void) {
	cin.tie(0)->sync_with_stdio(0);

	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> maze[i];
	}

	Time[0][0] = 1;
	myQueue.push({ 0,0 });
	while (!myQueue.empty()) {
		pair<int, int> cur = myQueue.front(); myQueue.pop();
		for (int dir = 0; dir < 4; dir++) {
			int nx = cur.X + dx[dir];
			int ny = cur.Y + dy[dir];
			if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
			if (maze[ny][nx] == '0' || Time[ny][nx] != 0) continue;
			Time[ny][nx] = Time[cur.Y][cur.X] + 1;
			visit[ny][nx] = true;
			myQueue.push({ nx, ny });
		}
	}

	cout << Time[N-1][M-1];
	
	return 0;
}