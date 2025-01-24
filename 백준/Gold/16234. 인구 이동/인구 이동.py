from collections import deque
import copy

N, L, R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def bfs(a,b):
    
    people_cnt = A[a][b]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    united = [[a,b]]

    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < N and visited[nx][ny] == 0 and L<= abs(A[x][y]-A[nx][ny]) <=R:
                visited[nx][ny] = 1
                people_cnt += A[nx][ny]
                united.append([nx,ny])
                q.append((nx,ny))
    

    avg = people_cnt // len(united)
    for u in united:
        A[u[0]][u[1]] = avg
    return united


ans = 0

while True:
    
    visited = [[0] * N for _ in range(N)]
    check = 0
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i,j)
                if len(country) > 1:
                    check = 1
    if check == 0:
        print(ans)
        break
    ans += 1

