from collections import deque
import copy
n,m = map(int,input().split())

ices = [list(map(int, input().split())) for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny  = y + dy[k]
            #빙산남은곳만 돌기
            if 0<= nx < n and 0<= ny <m and visited[nx][ny] == 0 and ices[nx][ny]>0:
                visited[nx][ny] = 1
                q.append((nx,ny))
    return visited
       
ans = 0


while True:
    tmp = copy.deepcopy(ices)
    for i in range(n):
        for j in range(m):
            #아직 빙산이 있는 곳이라면
            if ices[i][j] > 0:
                minus = 0
                # 얼마나 빼야할지 동서남북 계산 
                for k in range(4):
                    nx = i + dx[k]
                    ny  = j + dy[k]
                    #주변조회할 때 이미 값이 갱신된 것들의 이전값으로 계산하기 위해 tmp사용
                    if 0<= nx < n and 0<= ny <m and tmp[nx][ny] == 0:
                        minus += 1
                if minus >= ices[i][j]:
                    ices[i][j] = 0
                else:
                    ices[i][j] -= minus

    #몇덩어리인지 체크
    check = 0
    
    visited =[[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            #빙산이 있으면서 아직 방문한적없는 덩어리일때 
            if ices[i][j] > 0 and visited[i][j] == 0:
                bfs(i,j,visited)
                check += 1
    ans += 1
    #종료조건시 종료
    if check >= 2:
        break
    elif check == 0:
        ans = 0
        break

    

print(ans)