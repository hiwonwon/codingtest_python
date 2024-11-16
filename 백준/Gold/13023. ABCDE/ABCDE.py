n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, depth):
    if depth == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visited[i] == 1:
            visited[i] = 1
            dfs(i, depth+1)
            visited[i] = 0

visited = [0]*n
for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(0)