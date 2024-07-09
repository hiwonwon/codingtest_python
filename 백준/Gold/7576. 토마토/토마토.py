from collections import deque
m, n = map(int, input().split())


tomatos = [list(map(int, input().split())) for _ in range(n)]
ans = 0


q = deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j] == 1:
            q.append((i,j))


def bfs():
    global ans
    visited = [[0] * m for _ in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while(q):
        x,y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            #범위안에 있는 좌표이며 익지않은 토마토여야함
            if 0<= nx <n and 0<= ny <m and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = tomatos[x][y] + 1
                visited [nx][ny] = 1
                q.append((nx,ny))


bfs()

ans = 0
for i in range(n):
    for j in range(m):
        #bfs함수 실행 후에 안익은 토마토가 있다면 -1 출력 
        if tomatos[i][j] == 0 :
            print(-1)
            exit(0)
    ans = max(ans,max(tomatos[i]))


print(ans-1)
