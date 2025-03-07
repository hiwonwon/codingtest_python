import sys
from collections import deque
input = sys.stdin.readline


def cheeze():
    ch_dq = deque()
    ch_dq.append([0,0])
    
    melt_q = deque()
    visited[0][0] = 1
    
    while ch_dq:
        xx,yy = ch_dq.popleft()
        
        for nx,ny in ((xx+1,yy),(xx-1,yy),(xx,yy+1),(xx,yy-1)):
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                
                if not lists[nx][ny]:
                    ch_dq.append([nx,ny])
                elif lists[nx][ny]:
                    melt_q.append([nx,ny])
    for x,y in melt_q:
        lists[x][y] = 0
    return len(melt_q)
n,m = map(int,input().split())
lists = [list(map(int,input().split())) for _ in range(n)]
sum_cheeze = 0
for x in lists:
    sum_cheeze += sum(x)

res = 0
while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]

    melt_cnt = cheeze()
    sum_cheeze -= melt_cnt
    
    res += 1
    if not sum_cheeze:
        print(res)
        print(melt_cnt)
        break
    

                