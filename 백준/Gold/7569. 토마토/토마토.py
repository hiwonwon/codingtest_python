m,n,h = map(int,input().split())


tomatos = []
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

for _ in range(h):
    tmp = []
    for  _ in range(n):
        tmp.append(list(map(int,input().split())))
    tomatos.append(tmp)

from collections import deque
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k] == 1 and visited[i][j][k] == False:
                q.append((i,j,k))
                visited[i][j][k] = True

def bfs():
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0,]
    dz = [0,0,0,0,1,-1]
    while(q):
        x,y,z = q.popleft()
        for i in range(6):
            nx = dx[i] +x
            ny = dy[i] +y
            nz = dz[i] +z
            if 0<= nx < h and 0<= ny < n and 0<= nz < m:
                if tomatos[nx][ny][nz]== 0 and visited[nx][ny][nz] == False:
                    tomatos[nx][ny][nz] = tomatos[x][y][z] + 1
                    q.append((nx,ny,nz))
                    visited[nx][ny][nz] = True

bfs()

ans = 0
for a in tomatos:
    for b in a:
        for c in b:
            #bfs 실행 후에도 안익은게 있는 경우
            if c == 0:
                print(-1)
                exit(0)
        ans = max(ans,max(b))
print(ans -1)