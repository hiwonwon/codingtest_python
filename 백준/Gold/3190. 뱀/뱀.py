from collections import deque

n = int(input())
graph = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 2

turns = {}
l = int(input())
for _ in range(l):
    x,c = input().split()
    turns[int(x)] = c

s = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
#처음엔 오른쪽 방향으로 가므로
idx = 0
graph[0][0] = 1
snake = deque([(0,0)])
x,y = 0,0

while True:
    s += 1
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0>nx or 0>ny or nx>=n or ny>=n or (nx,ny) in snake:
        break
    #사과가 없으면 꼬리 없애기
    if graph[nx][ny] != 2:
        a,b = snake.popleft()
        graph[a][b] = 0
    x,y = nx,ny
    graph[x][y] = 1
    snake.append((x,y))



    #방향전환을 할때가 됐다면 처리
    if s in turns.keys():
        if turns[s] == "L":
            idx = idx-1
            if idx == -1:
                idx = 3
        else:
            idx = (idx+1)%4
    
print(s)


