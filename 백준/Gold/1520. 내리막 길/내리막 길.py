#상하좌우 이동가능
#시작: 가장 왼쪽 위 -> 제일 오른쪽아래 
#항상 높이가 더 낮은 지점으로만 이동(현재높이보다 낮은곳)
#범위: M,N <= 500
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


m,n = map(int,input().split())

visited = [[-1] * n for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):

    if x == m-1  and y == n -1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < m and 0<= ny < n and graph[x][y] > graph[nx][ny]:
            visited[x][y] += dfs(nx,ny)
    


    return visited[x][y]


graph = [list(map(int,input().split())) for _ in range(m)]

print(dfs(0,0))