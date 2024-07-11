n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []

#치킨집과 집이있는 좌표의 값을 따로 리스트에 받아줌
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append([i+1,j+1])
        if graph[i][j] == 2:
            chicken.append([i+1,j+1])
from itertools import combinations

ans = float('inf')
for c in combinations(chicken,m):
    #m개의 치킨집 고르는 것 반복
    temp = 0

    for h in home:
        #각 집에 가장 가까운 치킨집의 치킨거리 구함
        cd = float('inf')
        for j in range(m):
            cd = min(cd,abs(h[0]-c[j][0])+abs(h[1]-c[j][1]))
        #해당 집에서 가장 가까운 치킨집의 치킨거리 도시의 치킨거리에 구해줌
        temp += cd
    #구한 도시의 치킨거리중 최솟값 구함
    ans = min(ans,temp)

print(ans)