import sys
from collections import deque

n,m =map(int,sys.stdin.readline().split())

miro = []
visited = [[0]*m for i in range(n)]

for i in range(n):
    miro.append(list(map(int,sys.stdin.readline().rstrip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #x와 y가 범위내에 있고 이동할 수 있는 칸이며 아직 방문 안한곳일때
            if 0<=nx<n and 0<=ny<m and miro[nx][ny]==1 :
                q.append((nx,ny))
                miro[nx][ny] = miro[x][y]+1
    return miro[n-1][m-1]

print(bfs(0,0))