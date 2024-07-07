n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]


ans = 0
dp = [[0]*n for _ in range(n)] 
dp [0][0] = 1

def sol():
    for i in range(n):
        for j in range(n):
            k = graph[i][j]
            if k == 0 or dp[i][j] == 0:
                continue
            #아래쪽으로 이동하는 경우
            if i + k < n:
                dp[i+k][j] += dp[i][j]
            #오른쪽으로 이동하는 경우
            if j+k < n :
                dp[i][j+k] += dp[i][j]
    return dp[-1][-1]

print(sol())