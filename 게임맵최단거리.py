from collections import deque
def solution(maps):

    q = deque()
    n = len(maps) #y좌표 길이
    m = len(maps[0])  #x좌표 길이
    # visited = [[False]*m for i in range(n)]
    q.append((0,0))  #시작노드  두원소를 가진 튜플 추가
    # visited[0][0] = True #시작노드
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    while q:
        y,x = q.popleft()

        for i in range(4): #상하좌우 4번 반복  
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 :
                # if not visited[ny][nx]:
                    # visited[ny][nx] = True
                    q.append((ny,nx))
                    maps[ny][nx] = maps[y][x]+1  #현재까지 누적 거리에 +1
                    
        
        answer = maps[n - 1][m - 1]

    if answer == 1: 
        answer=-1
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))