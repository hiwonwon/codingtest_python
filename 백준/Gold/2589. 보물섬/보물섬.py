from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(startx, starty):
    visited = [[-1]*m for _ in range(n)]
    visited[startx][starty] = 0
    q = deque()
    q.append((startx, starty))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == -1 and board[nx][ny] == "L":
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return max(map(max, visited))
    
n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            ans = max(ans, bfs(i,j))

print(ans)