#파일 두개씩 계속 합쳐서 합쳐 나감 / 두파일 합칠때 시간 = 두 파일 크기의 합
#파일 합칠때 최소 비용?
import sys

t = int(input())
for _ in range(t):
    k = int(input())
    files = [0]+ list(map(int, input().split()))
    
    noojuck = [0] * (k+1)
    for i in range(1,k+1):
        noojuck[i] = noojuck[i-1] + files[i]
    
    dp = [[0]*(k+1) for _ in range(k+1)]
    for cnt in range(1,k):
        for start in range(1,k-cnt+1):
            end = start+cnt
            #구간 합칠 때의 최소 비용 구함
            mini = sys.maxsize
            for mid in range(start,end):
                mini = min(mini,dp[start][mid] + dp[mid+1][end])
            
            dp[start][end] = mini + noojuck[end] - noojuck[start-1]

    print(dp[1][k])