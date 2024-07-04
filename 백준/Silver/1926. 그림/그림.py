from collections import deque
n,m = map(int, input().split())
paint = []
for _ in range(n):
    paint.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]

def bfs (x,y):
    q =deque()
    q.append((x,y))
    dx= [-1,1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = 1
    cnt = 1
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx <n and 0<= ny <m and visited[nx][ny] == 0 and paint[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append((nx,ny))
                cnt+=1
    return cnt

ans = 0
ans1 = 0
for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and visited[i][j] == 0:
            ans1+=1
            ans = max(ans, bfs(i,j))

print(ans1)
print(ans)