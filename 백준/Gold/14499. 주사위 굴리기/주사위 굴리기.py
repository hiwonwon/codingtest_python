n,m,x,y,k = map(int,input().split())
graph = []

for i in range(n):
    temp = list(map(int,input().split()))
    graph.append(temp)

move = list(map(int,input().split()))


dice = [0,0,0,0,0,0]

def turn(direction):
    d1, d2, d3, d4, d5, d6 = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d4,d2,d1,d6,d5,d3
    elif direction == 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d3,d2,d6,d1,d5,d4
    elif direction == 3:
         dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d5,d1,d3,d4,d6,d2
    elif direction == 4:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = d2,d6,d3,d4,d1,d5

dx = [0,0,-1,1]
dy = [1,-1,0,0]
nx,ny = x,y
for i in move:
    nx += dx[i-1]
    ny += dy[i-1]
    if  nx >= n or nx<0 or ny >= m or ny<0:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue

    turn(i)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
        
    print(dice[0])
    

        


