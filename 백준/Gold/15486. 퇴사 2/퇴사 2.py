n = int(input())
counsel = [[0,0]]
for i in range(n):
    t, p = map(int, input().split())
    counsel.append([t,p])

dp =[0] * (n+1)

for i in range(1,n+1):
    t,p = counsel[i][0], counsel[i][1]
    dp [i] = max(dp[i],dp[i-1])
    end = i+t-1 #당일부터 t일 걸리므로 당일 포함하기 위해 -1
    if end <= n:
        #i일 부터 일해야 하므로 i-1일에다가 p를 더해줌
        dp[end] = max(dp[i-1] + p , dp[end])
print(max(dp))