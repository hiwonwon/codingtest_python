import sys
sys.setrecursionlimit(10**6)
A = list(input())
B = list(input())
dp = [[0]*(len(B)+1) for i in range(len(A)+1)]
path = []

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            continue
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])

def func(r, c):
    if r == 0 or c == 0:
        return 
    if A[r-1] == B[c-1]:
        path.append(A[r-1])
        func(r-1, c-1)
        return
    if dp[r-1][c] > dp[r][c-1]:
        func(r-1, c)
        return
    func(r, c-1)

func(len(A), len(B))
print(*reversed(path), sep='')