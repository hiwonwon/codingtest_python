import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())

max_num = 100000
visited = [0]*(max_num+1)
 
def bfs():
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        #목표위치에 도착하면 해당 
        if x == k:
            print(visited[x])
            break
        
        for j in (x-1,x+1,x*2):
            if 0<=j<=max_num and visited[j]==0:
                visited[j] = visited[x]+1
                q.append(j)
    return
bfs()