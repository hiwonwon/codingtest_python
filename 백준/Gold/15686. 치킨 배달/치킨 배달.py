import sys

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append([i,j])
        elif board[i][j] == 1:
            house.append([i,j])

target = []
chick_len = len(chicken)
arr = [[0,0] for _ in range(m)]
visited = [0]*m


min_chicken_dis = sys.maxsize


def dfs(start, cnt):
    global min_chicken_dis
    global chicken_dis
    if cnt==m:
        city_chicken = 0
        for h in range(len(house)):
            chicken_dis = sys.maxsize
            for i in range(m):
                dis = abs(arr[i][0]-house[h][0]) + abs(arr[i][1]-house[h][1])
                chicken_dis = min(chicken_dis,dis)
            city_chicken += chicken_dis
        min_chicken_dis = min(min_chicken_dis,city_chicken)
        return

    for i in range(start,chick_len):
        arr[cnt][0],arr[cnt][1] = chicken[i][0],chicken[i][1]
        dfs(i+1, cnt+1)

dfs(0,0)

print(min_chicken_dis)


