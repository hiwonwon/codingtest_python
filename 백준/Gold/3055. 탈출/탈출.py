from collections import deque

r,c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]



dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(si,sj):

    visited[si][sj] = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <r and 0<= ny <c:
                if (graph[nx][ny] =='.' or graph[nx][ny] == "D") and graph[x][y] == 'S':
                        visited[nx][ny] = visited[x][y] +1
                        graph[nx][ny] = 'S'
                        q.append((nx,ny))

                elif (graph[nx][ny] =='.' or graph[nx][ny] == "S") and graph[x][y] == '*':
                        graph[nx][ny] = '*'
                        q.append((nx,ny))



q = deque()

for i in range(r):
    for j in range(c):
        #고슴도치위치저장
        if graph[i][j] == 'S':
            si,sj = i,j
            q.append((si,sj))

for i in range(r):
    for j in range(c):
        #비버의 굴 위치 저장
        if graph[i][j] == "D":
            di = i
            dj = j

for i in range(r):
    for j in range(c):
        if graph[i][j] == "*":
            wi = i
            wj = j
            q.append((wi,wj))




bfs(si,sj)

if visited[di][dj]:
    print(visited[di][dj] - 1)
else:
    print("KAKTUS")