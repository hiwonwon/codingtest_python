import sys

N, M = map(int, sys.stdin.readline().split())
G = []

for i in range(N):
    S = list(map(int, sys.stdin.readline().split()))
    G.append(S)

cnt = 0
ret = 0
for i in range(N):
    for j in range(M):
        if G[i][j] == 1:
            cnt += 1
            s = 1
            stk = [(i, j)]
            G[i][j] = 0
            while stk:
                r, c = stk.pop()
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < N and 0 <= nc < M and G[nr][nc] == 1:
                        stk.append((nr, nc))
                        G[nr][nc] = 0
                        s += 1
            ret = max(ret, s)

print(cnt)
print(ret)