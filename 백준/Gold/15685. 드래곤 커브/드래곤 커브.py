n = int(input())
graph = [[0]*101 for _ in range(101)]
dragon = []

dx = [0,-1,0,1]
dy = [1,0,-1,0]

for _ in range(n):
    #순서 평소에 쓰던대로 전환
    y,x,d,g = map(int,input().split())
    graph[x][y] = 1
    prev = [d]
    q = [d]
    #세대만큼 반복
    for _ in range(g+1):
        for k in q:
            x += dx[k]
            y += dy[k]
            graph[x][y] = 1
        q = [(i+1)%4 for i in prev]
        q.reverse()
        prev += q
        


ans = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i][j+1] == 1 and  graph[i+1][j] == 1 and graph[i+1][j+1]==1:
            ans += 1
print(ans)