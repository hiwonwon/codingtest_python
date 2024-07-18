n, m = map(int, input().split())
start = list(map(int, input().split()))
rooms = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
visited = [[0]*m for _ in range(n)]


ans = 0
x,y,d = start[0] , start[1], start[2]
q = deque()
q.append((x,y,d))

visited[x][y] = 1
#시작하는 곳이 청소가 안된 빈칸일 때
if rooms[x][y] == 0:
    ans += 1
    #청소된 곳은 2로 표시
    rooms[x][y] = 2
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while(q):
    x,y,d = q.popleft()

    #주변 4칸 확인
    check = False
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx <n and 0<= ny <m and rooms[nx][ny] == 0:
            check =True

    #주변 4칸 중 청소되지 않은 칸이 있는 경우
    if check:
        #반시계 방향으로 90도 회전
        if d == 0:
            nd = 3
        else:
            nd = d-1

        # 앞쪽 칸으로 전진후 좌표 구하기
        if nd == 0:
            nx = x -1
            ny = y
        elif nd ==1:
            nx = x
            ny = y+1
        elif nd == 2:
            nx = x+1
            ny = y
        elif nd == 3:
            nx = x
            ny = y-1
        #전진할 좌표가 청소되지 않은 빈칸인경우에 전진
        if 0<= nx <n and 0<=  ny < m  and rooms[nx][ny]==0:
            q.append((nx,ny,nd))
            ans += 1
            #청소된 곳은 2로 표시
            rooms[nx][ny] = 2
        #청소되지않은 빈칸이 주변에 있지만 현재의 반시계방향으로 전진했을 때 빈칸이 아닌 경우
        else:
            q.append((x,y,nd))
    #주변4칸중 청소되지않은 빈칸 없을 경우
    else:
        if d == 0:
            nx = x+1
            ny = y
        elif d ==1:
            nx = x
            ny = y-1
        elif d == 2:
            nx = x -1
            ny = y
        elif d == 3:
            nx = x
            ny = y+1
        if 0<= nx <n and 0<=  ny < m  and rooms[nx][ny]!=1:
            q.append((nx,ny,d))
        if rooms[nx][ny]==1:
            print(ans)
            exit()
print(ans)                


