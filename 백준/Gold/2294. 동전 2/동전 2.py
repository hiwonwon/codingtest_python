n, k =map(int, input().split())
coins = [int(input()) for _ in range(n)]
#중복 제거
coins = list(set(coins))
coins.sort()
inf = float('inf')
dp = [inf] * (k+1)
dp[0] = 0

for c in coins:
    #현재 동전보다 작은 값은 갱신되지 않으므로 현재 동전의 값부터 시작
    for i in range(c,k+1):
        dp[i] = min(dp[i],dp[i-c]+1)



#불가능한 경우
if dp[k]>10000:
    print(-1)
else:
    print(dp[k])
