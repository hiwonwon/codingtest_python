n,k = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]

mx = 0
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(0,n):
    for j in range(1,k+1):
        if nlist[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], nlist[i][1] + dp[i-1][j-nlist[i][0]])

print(dp[n-1][k])