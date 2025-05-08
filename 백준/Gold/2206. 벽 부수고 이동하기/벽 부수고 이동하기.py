#0 이동가능 / 1 이동불가능
#1.1 -> n,m 이동 / 최단경로로 이동 = 가장 적은 개수의 칸을 지나는 것 
#벽 한개 부수기 
#불가능 -1
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0,0))

    while(q):
        x,y,cnt = q.popleft()
        if x == n-1  and  y == m-1:
            return visited[x][y][cnt]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                #다음에 이동할 곳이 아직 파괴하지 않은 벽
                if graph[nx][ny] == 1 and cnt == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx,ny,1))
                #다음에 이동할 곳이 벽이아니고 아직 방문하지 않은곳
                elif graph[nx][ny] == 0 and visited[nx][ny][cnt] == 0:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    q.append((nx,ny,cnt))
    return -1


print(bfs())
