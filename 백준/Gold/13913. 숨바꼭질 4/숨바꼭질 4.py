import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
visit = [0] * 100_001
move = [0] * 100_001

q = deque()
q.append(n)
ans = 0
cnt = 0

while(q):
    x = q.popleft()
    if x == k:
        break
    for nx in x+1,x-1,x*2:
        if 0<= nx <100_001:
            if visit[nx]==0 or visit[nx] >= visit[x]+1:
                q.append(nx)
                visit[nx] = visit[x] + 1
                #이전 노드를 저장하는 배열
                move[nx] = x


print(visit[k])

arr = []
tmp = k
for _ in range(visit[x]+1):
    arr.append(tmp)
    tmp = move[tmp]
print(' '.join(map(str, arr[::-1])))