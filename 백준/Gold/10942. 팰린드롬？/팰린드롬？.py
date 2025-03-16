import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int,input().split())]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1:
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 1
        else:
            dp[i][i+1] = 0

for gap in range(2, n):
    for i in range(n-gap):
        if arr[i] == arr[i+gap] and dp[i+1][i+gap-1]:
            dp[i][i+gap] = 1

m = int(input())
for _ in range(m):
    s, e = map(int,input().split())
    print(dp[s-1][e-1])