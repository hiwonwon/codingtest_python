from sys import stdin

def _1915(n, m, arr):
    l = 0
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if l < dp[i][j]:
                    l = dp[i][j]
    
    print(l ** 2)

if __name__ == "__main__":
    input = stdin.readline
    arr = []
    n, m = map(int, input().split())
    for _ in range(n):
        arr.append(list(map(int, list(input().strip()))))

    _1915(n, m, arr)