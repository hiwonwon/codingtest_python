#수빈 1초 후 x-1,x+1,2*x 범위 10만-> 이중for문 가능
#가장 빠른시간, 방법의 수
#알고리즘: bfs? 

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
visit = [0] * 100_001

q = deque()
q.append(n)
ans = 0
cnt = 0

while(q):
    x = q.popleft()
    if x == k:
        cnt +=1
        continue

    for nx in x+1,x-1,x*2:
        if 0<= nx <100_001:
            if visit[nx]==0 or visit[nx] >= visit[x]+1:
                q.append(nx)
                visit[nx] = visit[x] + 1

print(visit[k])
print(cnt)