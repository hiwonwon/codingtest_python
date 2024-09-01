n, a = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
ns = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        ns[i][j] = arr[i-1][j-1] + ns[i-1][j] + ns[i][j-1] - ns[i-1][j-1]

for i in range(a):
    p, q, r, s = map(int, input().split())
    print(ns[r][s] - ns[p-1][s] - ns[r][q-1] + ns[p-1][q-1])
