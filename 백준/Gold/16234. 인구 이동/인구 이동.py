import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x, y):
    queue = deque([(x, y)])
    union = [(x, y)]
    total_population = a[x][y]
    chk[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not chk[nx][ny]:
                if l <= abs(a[cx][cy] - a[nx][ny]) <= r:
                    chk[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += a[nx][ny]

    return union, total_population

days = 0

while True:
    chk = [[False] * n for _ in range(n)]
    move = False

    for i in range(n):
        for j in range(n):
            if not chk[i][j]:
                union, total_population = bfs(i, j)
                if len(union) > 1:
                    move = True
                    new_population = total_population // len(union)
                    for x, y in union:
                        a[x][y] = new_population

    if not move:
        print(days)
        break
    days += 1