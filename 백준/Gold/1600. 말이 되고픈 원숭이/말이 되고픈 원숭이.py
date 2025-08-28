#x표시한 곳으로 말이 갈 수 있음, 장애물도 뛰어넘음
#원숭이는 k번만 말처럼 이동, 그외에는 상하좌우, 장애물 있는 곳으로는 이동 불가
#최소한의 동작으로 도착지점 가는경우는?
#범위 <= 200
from collections import deque



        
        

k = int(input())
w,h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * w for _ in range(h)] for _ in range(k+1)]


q = deque()
q.append((0,0,0))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

mx = [-2,-1,-2,-1,2,1,2,1]
my = [-1,-2,1,2,-1,-2,1,2]

visited[0][0][0] = 1
flag = True

while(q):
    cnt,x,y = q.popleft()

    if (x == h-1 and y == w-1):
        print(visited[cnt][x][y]-1)
        flag = False
        break
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<h and 0<= ny <w and visited[cnt][nx][ny] == 0 and graph[nx][ny] != 1:
            q.append((cnt,nx,ny)) 
            visited[cnt][nx][ny] = visited[cnt][x][y] + 1
    
    if cnt < k:
           for i in range(8):
                nx = mx[i] + x
                ny = my[i] + y
                if 0<=nx<h and 0<= ny <w and visited[cnt+1][nx][ny] == 0 and graph[nx][ny] != 1:
                    q.append((cnt+1,nx,ny))
                    visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1


if flag:
    print(-1)


