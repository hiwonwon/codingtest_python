from collections import deque

N, M = map(int, input().split())
board = []
visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(N):
    string = input()
    line = []

    for s in string:
        line.append(s)

    board.append(line)


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def bfs(a, b):
    max_t = 0
    visited[a][b] += 1
    if max_t < visited[a][b]:
        max_t = visited[a][b]
    q = deque([(a, b)])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = visited[x][y] + 1
                if max_t < visited[nx][ny]:
                    max_t = visited[nx][ny]
                q.append((nx, ny))

    return max_t

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            max_t = bfs(i, j)

            if result < max_t:
                result = max_t

            visited = [[0 for _ in range(M)] for _ in range(N)]

print(result-1)