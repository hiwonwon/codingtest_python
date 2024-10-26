import sys
input = sys.stdin.readline

def check(s, e):
    prv = log[0]
    cur = abs(arr[s] + arr[e])

    if cur < prv:
        log[0], log[1], log[2] = cur, arr[s], arr[e]

N = int(input())
arr = list(map(int, input().split()))

s = 0
e = N - 1
log = [sys.maxsize, 0, 0]
while s < e:
    check(s, e)

    if arr[s] + arr[e] > 0:
        e -= 1
    elif arr[s] + arr[e] < 0:
        s += 1
    else:
        s += 1
        e -= 1



ans = sorted(log[1:])
print(*ans)