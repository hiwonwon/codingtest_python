# 1389. 케빈 베이컨의 6단계 법칙 (2024.6.10) | S1
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
  
def bfs(start):
  num = [0] * (N + 1)
  visited = [start]
  queue = deque()
  queue.append(start)
  
  while queue:
    a = queue.popleft();
    for g in graph[a]:
      if g not in visited:
        num[g] = num[a] + 1
        visited.append(g)
        queue.append(g)
        
  return sum(num)

result = []
    
for i in range(1, N+1):
  result.append(bfs(i))
  
print(result.index(min(result)) + 1)