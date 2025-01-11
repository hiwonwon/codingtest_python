from collections import deque
import sys


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]


dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(a,b,cnt):
    global ans

    ans = max(cnt,ans)
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<= nx < r and 0<= ny < c:
            if board[nx][ny] not in alpha:
                alpha.add(board[nx][ny])
                dfs(nx,ny,cnt+1)
                alpha.remove(board[nx][ny])


ans = 0
alpha= set(board[0][0])
dfs(0,0,1)
print(ans)