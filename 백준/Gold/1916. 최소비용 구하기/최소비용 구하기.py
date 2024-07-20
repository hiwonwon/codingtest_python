import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    s,e,p = map(int,input().split())
    graph[s].append([e,p])

start , dest = map(int,input().split())
costs = [1e9 for _ in range(n+1)]
heap = []
costs[start] = 0
heapq.heappush(heap,[0,start])

while(heap):
    cur_p, cur_v = heapq.heappop(heap)
    if costs[cur_v] < cur_p:
        continue
    for  next_v, next_p in graph[cur_v]:
        sum_c = cur_p + next_p 
        if sum_c < costs[next_v]:
            costs[next_v] = sum_c
            heapq.heappush(heap,[sum_c, next_v])
print(costs[dest])
 