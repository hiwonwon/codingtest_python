#16928 Gold 5

import sys 
from collections import deque

input = sys.stdin.readline

def BFS():     
        
    while(True):
        pop = q.popleft()
        #print(" ".join(f"{x:<3d}" for x in visit))
        if pop == 100:
            break 
        
        if pop in ladderSnake.keys():
            val = ladderSnake[pop]
            visit[val-1] = visit[pop-1]
            q.appendleft(val)        
            continue        
        
        num = pop
            
        for _ in range(1,7):
            num += 1
            
            if num == 100:
                visit[num-1] = visit[pop-1]+1
                q.appendleft(num)
                break
            
            if not visit[num-1]:
                visit[num-1] = visit[pop-1]+1
                q.append(num)
        #print("")
    return visit.pop()
    
n , m = map(int, input().split())
visit = [False] * 100

ladderSnake = {}

q = deque([1])

for i in range(n+m):
    tmp = list(map(int,input().split()))
    ladderSnake[tmp[0]] = tmp[1]
    
print(BFS())