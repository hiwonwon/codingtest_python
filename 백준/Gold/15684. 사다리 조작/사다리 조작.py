#인접한 세로선 사이에 가로선 한개 둠
#가로선끼리 접하거나 연속되면 안됨
#i번의 세로선 결과가 i번이 나와야함
#그러기 위한 추가해야할 가로선 최솟값은?
#정답이 3보다 크면 -1 불가능해도 -1
#모든 점이 i -> i인지 체크
def check():
    for i in range(n):
        now = i
        for j in range(h):
            if graph[j][now] == 1:
                now += 1
            elif now >0 and graph[j][now-1] == 1:
                now -=1
        if now != i :
            return False
    return True


def dfs(cnt,x,y):
    global ans
    if check():
        ans = min(ans,cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    #행 먼저 탐색
    for i in range(x,h):
        if i == x:
            now = y
        else:
            now = 0

        for j in range(now,n-1):
            #오른쪽에 사다리 없을때
            if graph[i][j] != 1 and graph[i][j+1] != 1:
                #왼쪽에 사다리 있을때
                if j>0 and graph[i][j-1] == 1:
                    continue
                #왼쪽에 사다리 없을 때 즉 오른쪽에 추가 가능함
            
                graph[i][j] = 1
                dfs(cnt+1, i, j+2)
                graph[i][j] = 0

n,m,h = map(int,input().split())
graph = [[0]*(n) for _ in range(h)]

for _ in range(m):
    a, b =  map(int,input().split())
    graph[a-1][b-1] = 1

ans = 4

dfs(0,0,0)
print(ans if ans < 4 else -1)


