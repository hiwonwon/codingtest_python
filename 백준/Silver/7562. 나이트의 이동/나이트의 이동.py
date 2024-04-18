from collections import deque

n = int(input())

for _ in range(n):
    ii = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    graph = [[0]*ii for _ in range(ii)]

    q = deque()
    q.append((a,b))
    dx = [-2,2,-1,1]
    dy = [1,-1,-2,2]

    while(q):
        x,y = q.popleft()
        if x == c and y == d:
            break
        for i in range(2):
            for j in range(2):
                nx = x+dx[i]
                ny = y+dy[j]
                if 0<=nx<ii and 0<=ny<ii and graph[nx][ny]==0:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
        for i in range(2,4):
            for j in range(2,4):
                nx = x+dx[i]
                ny = y+dy[j]
                if 0<=nx<ii and 0<=ny<ii and graph[nx][ny]==0:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
    print(graph[c][d])

