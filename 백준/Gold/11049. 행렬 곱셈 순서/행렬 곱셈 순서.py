n = int(input())
m = []
for _ in  range(n):
    r,c = map(int,input().split())
    m.append((r,c))

dp = [[0 ]* n for _ in range(n)]

for cnt in range(n-1):
    for i in range(n-cnt-1):
        j = cnt+i+1
        dp[i][j] = 2**31
        for k in range(i,j):
            dp[i][j] = min (dp[i][j],dp[i][k]+dp[k+1][j]+m[i][0]*m[k][1]*m[j][1])

print(dp[0][n-1])
