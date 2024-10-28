from collections import deque

Y, X = map(int, input().split())
bomul_map = [list(input().rstrip()) for _ in range(Y)]

maxi = 0
for y in range(Y):
    for x in range(X):
        if bomul_map[y][x] == 'L':
            visited = [[0] * X for _ in range(Y)]
            dist = [[0] * X for _ in range(Y)]

            # BFS
            q = deque()
            q.append((y, x))
            visited[y][x] = 1

            while len(q) > 0:
                c_y, c_x = q.popleft()
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = c_y + dy, c_x + dx
                    if 0 <= ny < Y and 0 <= nx < X and bomul_map[ny][nx] == 'L':
                        if visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            dist[ny][nx] = max(dist[c_y][c_x]+1, dist[ny][nx])
                            maxi = max(maxi, dist[ny][nx])
                            q.append((ny, nx))


print(maxi)
