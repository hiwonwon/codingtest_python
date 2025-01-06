from collections import deque
from copy import deepcopy 
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    tmp = deepcopy(graph)
    q = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
    
    

    dx = [-1,1,0,0]
    dy = [0,0,1,-1]


    while(q):
        a,b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<= x <n and 0<= y <m and tmp[x][y] == 0:
                tmp[x][y] = 2
                q.append((x,y))
    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp[i].count(0)

    #안전영역 더 큰걸로 답 갱신
    answer = max(answer,cnt)
    return answer

def makeWall(cnt):

    if cnt == 3:
        bfs()
        return answer
    
    for i in range(n):
        for j in range(m):
            # 벽을 세울 수 있다면
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0


answer = 0
makeWall(0)
print(answer)