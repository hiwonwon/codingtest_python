import sys

input = sys.stdin.readline

str1 = [''] + list(input().rstrip())
str2 = [''] + list(input().rstrip())

n1 = len(str1)
n2 = len(str2)

dp = [['']*n1 for _ in range(n2)]
for i in range(1,n2):
    for j in range(1,n1):
        if str1[j] == str2[i]:
            dp[i][j] = dp[i-1][j-1] + str1[j]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

ans = len(dp[-1][-1])
print(ans)
if ans!= 0 :
    print(dp[-1][-1])