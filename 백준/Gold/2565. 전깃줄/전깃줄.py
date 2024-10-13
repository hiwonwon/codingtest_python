n = int(input())
ab = []
for i in range(n):
    a,b = map(int, input().split())
    ab.append([a,b])

ab.sort(key = lambda x:x[0])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if ab[i][1]> ab[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))
