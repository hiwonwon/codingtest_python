n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [float('inf')] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        if dp[i] > (dp[i - coin] + 1):
            dp[i] = dp[i - coin] + 1

print(dp[k] if dp[k] < float('inf') else -1)
