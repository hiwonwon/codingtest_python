n = int(input())
a = list( map(int,input().split()) )

dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
x = max(dp)
ans  = []
for i in range(n-1,-1,-1):
    if dp[i] == x:
        ans.append(a[i])
        x -=1
ans.reverse()
print(*ans)