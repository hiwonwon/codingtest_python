#가장자리에서 탈출 즉 0이거나 n or m이거나
#탈출여부 -> 탈출한다면 걸리는 시간
# 불은 상하좌우로 확산(벽제외하고)
#지훈이가 이동하는 동안 불이 매초마다 좌우상하로 확산되어야함
#J 매초마다 이동-> F가 퍼질 수 있는 방향에 있는애들은 제거
# 알고리즘: bfs
#범위 1000
from collections import deque
r,c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
#지훈이의 위치
q_jh = deque()
#불의 위치
qf = deque()
dist = [[int(1e9)] * c for _ in range(r)]
ans = 0
visited_f = [[0]*c for _ in range(r)]
visited_j = [[0]*c for _ in range(r)]
dx = [0,0,0-1,1]
dy = [1,-1,0,0]


for i in range(r):
    for j in range(c):
        if graph[i][j] == "J":
            q_jh.append((i,j))
            visited_j[i][j] = 1
        elif graph[i][j] == "F":
            qf.append((i,j))
            visited_f[i][j] = 1
            

def bfs():
    while qf:
        x, y = qf.popleft()

        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if not visited_f[nx][ny] and graph[nx][ny] != "#":
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    qf.append((nx, ny))
    while q_jh:
        x, y = q_jh.popleft()

        for i in range(4):
            nx, ny = x +dx[i], y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != "#" and not visited_j[nx][ny]:

                    if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        q_jh.append((nx, ny))
            else:
                return visited_j[x][y]
    return 'IMPOSSIBLE'



print(bfs())