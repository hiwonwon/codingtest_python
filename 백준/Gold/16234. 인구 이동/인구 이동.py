from collections import deque
N,L,R = map(int,input().split()) #땅크기, L이상 R이하
graph = []
visited = [[False]*N for _ in range(N)]
teams=[]
dx=[0,0,-1,1] #상하좌우
dy=[-1,1,0,0]
#맵 입력
for _ in range(N):
    graph.append( list(map( int, input().split() )) )

def bfs(graph, x, y):
    population = graph[y][x]
    visited[y][x] = True
    q=deque([(x,y,graph[y][x])])
    team=[(x,y)]
    while q:
        x,y,p = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == False:
                if L<=abs(graph[ny][nx]-p)<=R:
                    visited[ny][nx] = True
                    team.append( (nx,ny) )
                    population += graph[ny][nx]
                    q.append( (nx,ny,graph[ny][nx]) )
    return (population, team)
        
#탐색
day = 0
moving = True
while True:
    moving = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                population, team = bfs(graph, j, i) #튜플 반환
                if len(team) > 1:
                    moving=True
                    for tx,ty in team:
                        graph[ty][tx] = int(population/len(team))
    visited = [[False]*N for _ in range(N)]
    if moving == False:
        break
    else:
        day+=1

print(day)