#상하좌우 이동
#이전지역보다 대나무 많이 있는 곳으로 이동
#어떤 지점에 놓았을때 판다가 이동할 수 있는 최대 칸 수??
#n<= 500
#알고리즘: bfs?
from sys import setrecursionlimit 
setrecursionlimit(10**9)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    #한번도 방문 안한 곳만 방문
    if dp[x][y] < 0 :
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and  0<=ny<n and graph[x][y]<graph[nx][ny]:
                dp[x][y] = max(dp[x][y],dfs(nx,ny))
        dp[x][y] += 1
    return dp[x][y]


ans = 0
dp = [[-1]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans)
        

    

