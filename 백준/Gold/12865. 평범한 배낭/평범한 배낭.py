import sys

n,k = map(int,sys.stdin.readline().split())
arr = list()
for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    arr.append((w,v))
dp = [0]*100001
for a in arr:
    for i in range(k,a[0]-1,-1):
        dp[i] = max(dp[i-a[0]]+a[1],dp[i])
print(dp[k])
    