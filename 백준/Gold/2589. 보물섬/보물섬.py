import sys
from collections import deque
input = sys.stdin.readline

# 첫 번째 줄에서 n과 m을 읽음 (행의 수와 열의 수)
n, m = map(int, input().split())

# n개의 행을 지도 배열로 읽어들임
arr = [list(input().strip()) for _ in range(n)]


def bfs(a,b):
    ans = [[0]*m for _ in range(n)]
    q = deque()
    q.append((a,b))
    ans[a][b] = 1
    mx = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while(q):
        a,b = q.popleft()
        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b
            #범위안에 있고 육지이고 아직 방문한적없는 칸이면
            if 0<=x<n and 0<=y<m and arr[x][y] != 'W' and ans[x][y] == 0:
                ans[x][y] = ans[a][b] + 1
                mx = max(mx, ans[x][y])
                q.append((x,y))
    return mx-1

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            ans = max(ans,bfs(i,j))
print(ans)
