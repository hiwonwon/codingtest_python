import sys

input = sys.stdin.readline

N = int(input())
dp = [1] * 10

for _ in range(N - 1):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

ans = sum(dp)

print(ans % 10007)