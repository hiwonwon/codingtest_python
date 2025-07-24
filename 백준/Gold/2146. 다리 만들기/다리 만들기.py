#가장 짧은 다리를 놓을때 다리 길이
# == 육지간 거리중 최단거리
#모든 육지 방문하면서 다른 육지 만날때까지 bfs
#모든 좌표 방문하면서 같은 섬끼리 번호 같게 다른섬끼리 번호 다르게 두고
#다시 방문하면서 한 섬에서 다른섬 만날때까지 bfs 하고 최단거리 구하기

from collections import deque
import sys

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b,now):
    q  = deque()
    q.append((a,b))
    visited[a][b] = 1
    graph[a][b] = now
    
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if visited[nx][ny] == 0:
                #섬이면 방문
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    graph[nx][ny] = now
                    visited[nx][ny] = 1
land = 1
for i in range(n):
    for j in range(n):
        #아직 방문 안한 섬이라면 
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j,land)
            land += 1


def bfs2(island):
    q  = deque()
    dist = [[-1] * n for _ in range(n)]
 
    #미리 담아두기
    for i in range(n):
        for j in range(n):
            if graph[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0
    
    while(q):
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] != island and graph[nx][ny] != 0:
                return dist[x][y]
            if graph[nx][ny] == 0 and dist[nx][ny] == -1: # 물이고 아직 건너지 않은 곳일 경우
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return sys.maxsize



#다른 섬들끼리 번호가 다르게 설정한 후

ans = sys.maxsize
for island in range(1,land):
    ans = min (ans, bfs2(island))

print(ans)

