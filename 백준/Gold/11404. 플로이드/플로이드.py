import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dist = [[float('inf')  for _ in range(n + 1)] for _ in range(n+1) ] 
for i in range(m):
    a,b,c = map(int,input().split())
    dist[a][b] = min(c, dist[a][b])
for i in range(1,n+1):
    dist[i][i] = 0
    
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in dist[1:]:
    for j in i[1:]:
        if j == float('inf'):
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()