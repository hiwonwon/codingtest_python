#알고리즘 -> 다익스트라, bfs
#자기 크기와 같은 물고기 수를 먹어야 크기 1증가 -> 즉, 여태까지 먹은거 + 자기크기 알아야함
from collections import deque

n = int(input())
graph =[list(map(int,input().split())) for i in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
x, y, size = 0, 0, 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def bfs(a,b,size):
    visited = [[0]*n for _ in range(n)]
    dist =  [[0]*n for _ in range(n)]
    q = deque()
    q.append((a,b))

    visited[a][b] = 1
    tmp = []
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                
                if graph[nx][ny] <= size:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    #사이즈 작은 물고기 만날때 먹어야함
                    if 0 < graph[nx][ny] < size:
                        tmp.append((nx,ny,dist[nx][ny]))
            #거리가 가장 가까운것, 가장 왼쪽 , 가장 위에 있는 좌표가 삭제되도록
    return sorted(tmp,key=lambda x:(-x[2],-x[0],-x[1]))


cnt = 0
ans = 0

while 1:
    shark = bfs(x,y,size)
    
    if len(shark)== 0:
        break

    nx,ny, dis = shark.pop()
    ans += dis
    graph[x][y], graph[nx][ny] = 0,0
    x,y = nx,ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(ans)