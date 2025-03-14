#미로크기 N*M 빈방or 벽, 벽은 부숴야만 이동가능
#운영진 모두 같은방에 있어야함 , 상하좌우 한 칸 이동가능
#벽은 평소에는 불가능하나 무기사용해 벽->빈방 으로 변환 가능
#벽 !최소! 몇개 부수어야 하는지?

#범위: n,m<=100 // 최소로 부순다는 것 == 벽을 부술 일을 가장 적게 만들면서 목표지 도달
#알고리즘: BFS? 

from collections import deque
import heapq
m, n = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

dx = [1, 0, -1, 0]  # 행이동
dy = [0, 1, 0, -1]  # 열이동
visited = [[-1]*m for _ in range(n)]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0


    while(q):
        x,y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0>nx or nx>=n or 0>ny or ny>=m:
                continue
            
            if visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                   visited[nx][ny] = visited[x][y]
                   q.appendleft((nx,ny))
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                    

bfs()
print(visited[n-1][m-1])