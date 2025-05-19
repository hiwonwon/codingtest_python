# 알고리즘 -> 이분탐색? 큐? 스택?
from collections import deque
n,m = map(int,input().split())
graph = [[]for i in range(n+1)]
degree = [0 for i in range(n+1)]
answer = []
q = deque()

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    answer.append(tmp)
    for i in graph[tmp]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

print(*answer)

