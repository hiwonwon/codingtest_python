import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
tree = [[] for _ in range(n)]
visited = [False] * n
result = False

for _ in range(m):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def dfs(v, depth):
    global result

    visited[v] = True

    if depth == 4:
        result = True
        return

    for cur_v in tree[v] :
        if not visited[cur_v]:
            dfs(cur_v, depth + 1)

    visited[v] = False

for i in range(n):
    dfs(i, 0)
    if result: break

if result: print(1)
else: print(0)