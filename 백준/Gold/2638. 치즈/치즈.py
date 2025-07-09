import sys
import copy

from collections import deque
n,m = map(int, input().split())
graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

dx = [0,0,-1,1]
dy =[1,-1,0,0]

def bfs(a,b):
    q=deque()
    q.append((a,b))
    visited[a][b] = 1
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <n and 0<= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                #치즈 있는 곳의 방문횟수 체크
                elif graph[nx][ny] == 1:
                    visited[nx][ny] += 1



ans = 0
while True:
    
    visited = [[0]*m for _ in range(n)]
    bfs(0,0)
    for i in range(n):
        for j in range(m):
            #치즈가 있는 곳의 방문횟수가 2이상이면
            if visited[i][j] >= 2:
                graph[i][j] = 0
    ans += 1
    #치즈 다 사라지면 종료
    check = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                check+=1
    
    if check == 0:
        break
    

print(ans)

