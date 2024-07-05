from collections import deque

def bfs(i, k, visited):
  q = deque()
  q.append((i, k))
  visited[i][k] = 1
  size = 1
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1 ,1]
  while q:
    x, y = q.popleft()
    visited[x][y] = 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m :
        if visited[nx][ny] == 0 and board[nx][ny] == 1:
          q.append((nx, ny))
          visited[nx][ny] = 1
          size += 1
  return size 
    

n, m = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

cnt = 0
maxsize = 0
for i in range(n):
  for k in range(m):
    if visited[i][k] == 0 and board[i][k] == 1:
      size = bfs(i, k, visited)
      if size > maxsize :
        maxsize = size
      cnt += 1

print(cnt)
print(maxsize)