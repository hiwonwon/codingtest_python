import sys
input = sys.stdin.readline
import heapq

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dijk(n,graph):
    visit = [[1e10]*n for _ in range(n)]
    visit[0][0] = graph[0][0]
    h = []
    heapq.heappush(h,(visit[0][0],0,0))

    while(h):
        wei,x,y = heapq.heappop(h)
        if visit[x][y] < wei:
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx <n and 0<=ny<n:
                if wei + graph[nx][ny] < visit[nx][ny]:
                    visit[nx][ny] = wei + graph[nx][ny]
                    heapq.heappush(h,(visit[nx][ny],nx,ny))
    return visit[n-1][n-1]
tt = 1
while True:
    n = int(input())
    if n ==0:
        break
    graph = []
    for _ in range(n):
        tmp = list(map(int,input().split()))
        graph.append(tmp)

    ans = dijk(n,graph)
    print(f"Problem {tt}: {ans}")
    tt+=1
