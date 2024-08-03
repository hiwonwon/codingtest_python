from math import sqrt

TC = int(input())
for T in range(1, TC + 1):
    x, y = map(int, input().split())
    l = y - x
    n = int(sqrt(l))
    # 각 제곱에 매칭되는 홀수
    m = n * 2 - 1
    # n^2과 (n+1)^2의 반절보다 작다면..
    if l == n * n:
        print(m)
    elif n * n < l <= n * n + n:
        print(m + 1)
    elif n * n + n < l < n * n + 2 * n + 1:
        print(m + 2)
    elif l == (n + 1) * (n + 1):
        print(m + 2)