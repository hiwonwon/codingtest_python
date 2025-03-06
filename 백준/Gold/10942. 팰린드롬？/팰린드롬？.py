import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int,input().split()))
m = int(input())
dp = [[0]*n for _ in range(n)]
#길이가 1인 부분배열 처리
for i in range(n):
    dp[i][i] = 1
#길이가 2인 부분배열 처리
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

#cnt + 3 = 현재 확인하는 부분 배열의 길이
for cnt in range(n-2):
    for i in range(n-2-cnt):
        #i가 현재 확인하는 부분배열의 시작점 j는 끝점
        j = i+2+cnt
        if nums[i] == nums[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1


for _ in range(m):
    s,e = map(int,input().split())
    print(dp[s-1][e-1])

