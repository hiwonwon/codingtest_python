import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [list(str(sys.stdin.readline().strip())) for _ in range(N)]
L_list = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            L_list.append((i, j))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0
while L_list:
    x, y = L_list.pop(0)
    queue = deque([((x, y), 0)])
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1

    while queue:
        coordinate, count = queue.popleft()
        x, y = coordinate[0], coordinate[1]

        for i, j in directions:
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([(nx, ny), count + 1])
                result = max(result, count + 1)
print(result)
        