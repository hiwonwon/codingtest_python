import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

N = int(input())
visited = [[1]*N for _ in range(N)]
visited_redgreen = [[1]*N for _ in range(N)]
graph = [list(input()) for _ in range(N)]
graph_redgreen = [[1]*N for _ in range(N)]
for j in range(N):
    for k in range(N):
        graph_redgreen[j][k] = graph[j][k]
        if graph[j][k] == 'G':
            graph_redgreen[j][k] = 'R'
# print(graph,graph_redgreen)
def dfs(x,y,color,visited,graph):
    visited[x][y]= 0
    for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
        if 0 <= a+x < N and 0 <= b+y < N:
            if visited[a+x][b+y] and graph[a+x][b+y] == color:
                dfs(a+x,b+y,color,visited,graph)

cnt_mid = 0
cnt_redgren = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            cnt_mid += 1
            dfs(i,j,graph[i][j],visited,graph)
        if visited_redgreen[i][j]:
            cnt_redgren += 1
            dfs(i,j,graph_redgreen[i][j],visited_redgreen,graph_redgreen)

print(cnt_mid, cnt_redgren)