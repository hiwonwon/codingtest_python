import sys
sys.setrecursionlimit(10**6)

def DFS(x,y):
    global cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and visited[nx][ny] == 0 and maps[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt +=1
            DFS(nx,ny)

if __name__ == "__main__":


    count = 0
    cnt = 0
    result = []

    input = sys.stdin.readline
    m, n, k = map(int,input().split())
    maps = [[0]*n for _ in range(m)]
    visited = maps.copy()

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(k):
        ly, lx, ry, rx = map(int, input().split())
        for j in range(lx, rx):
            for k in range(ly, ry):
                maps[j][k] = 1


    
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 0 and visited[i][j] == 0:
                count +=1
                cnt +=1
                visited[i][j] = 1
                DFS(i,j)
                result.append(cnt)
                cnt = 0
    
    print(count)
    result.sort()
    print(' '.join(map(str,result)))