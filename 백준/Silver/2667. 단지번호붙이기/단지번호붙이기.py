import sys
from collections import deque




def bfs(graph, x,y):

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(graph)
    #apt = 0는 단지별 아파트 개수
    apt = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0 

    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                apt +=1
                #카운트 한 곳은 0으로 바꾸기
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return apt

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

ans = []

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            ans.append(bfs(graph, i, j))

print(len(ans))
for i in sorted(ans):
    print(i)