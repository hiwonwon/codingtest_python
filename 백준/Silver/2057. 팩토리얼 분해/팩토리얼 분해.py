import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * 21
dp[0] = 1
for i in range(1, 20):
    dp[i] = i * dp[i-1]

if N == 0:
    print("NO")
else:
    for i in range(20, -1, -1):
        if N >= dp[i]:
            N -= dp[i]

    if N == 0:
        print("YES")
    else:
        print("NO")