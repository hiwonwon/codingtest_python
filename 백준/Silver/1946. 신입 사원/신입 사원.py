import sys
t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort()
    max = arr[0][1]
    cnt = 1
    for i in range(1,n):
        if arr[i][1]<max:
            cnt+=1
            max = arr[i][1]
    print(cnt)