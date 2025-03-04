import copy
from collections import deque
r,c = map(int,input().split())
graph = []
for _ in range(r):
    row = list(map(int,input().split()))
    graph.append(row)
dx = [0,0,1,-1]
dy = [1,-1,0,0]


#구멍이 아닌 공기만 방문
def bfs():
    #판의 가장자리이므로 0,0은 항상 0임
    q=deque([(0,0)])
    visited[0][0] = 1

    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<r and 0<=ny<c and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
pre = 0
cnt = 0
t = 0
for g in graph:
    cnt += g.count(1)

while True:
    #치즈가 사라지면 종료
    cnt = 0
    for g in graph:
        cnt += g.count(1)
    if cnt == 0:
        break
    visited = [[0]*c for _  in range(r)]
    #구멍을 제외한 공기만 방문하는 함수
    bfs()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                #공기와 맞닿은 테두리 부분인지 체크
                check = False
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<= nx<r and 0<=ny<c and visited[nx][ny] == 1:
                        check = True
                        break
                #테두리면 삭제 진행
                if check:
                    graph[i][j] = 0
    pre = cnt
    t += 1


print(t)
print(pre)


