from collections import deque



def dfs(graph,a,b):
    q = deque()
    q.append((a,b))

    home_cnt = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    home_cnt+=1
    graph[a][b] +=1

    
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0<= ny < n and graph[nx][ny] == 1:
                q.append ((nx,ny))
                home_cnt+=1
                #visited 대신 값을 변경하여 방문여부 체크
                graph[nx][ny] = 0
    return home_cnt

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


home_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home_list.append(dfs(graph, i,j))

print(len(home_list))


for h in sorted(home_list):
    print(h)





        
