from collections import deque


def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    result = [0 for i in range(m+1)]
    visited = [[0]*m for _ in range(n)]
    dx = [-1,1,0 ,0]
    dy = [0,0,-1,1]
        
    def bfs(a,b):
        q = deque()
        q.append((a,b))
        min_y, max_y = b, b
        visited[a][b] =1
        cnt = 0
        while(q):
            x,y = q.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            cnt+=1
            
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        for i in range(min_y,max_y+1):
            result[i] += cnt
            
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] ==1:
                bfs(i,j)
    answer = max(result)
    return answer