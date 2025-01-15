n = int(input())
m = int(input())

inf = float("INF")

ans = [[inf]*(n+1) for _ in range(n+1)] 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            ans[i][j] = 0


for _ in range(m):
    a,b,c = map(int,input().split())
    ans[a][b] = min(ans[a][b],c)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            ans[i][j] = min(ans[i][j],ans[i][k]+ans[k][j])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if ans[a][b] == inf:
            print("0",  end=" ")
        else:
            print(ans[a][b], end=" ")
    print()