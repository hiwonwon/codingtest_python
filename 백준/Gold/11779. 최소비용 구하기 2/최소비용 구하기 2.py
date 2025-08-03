#다익스트라 최소비용
import heapq
inf = float("INF")

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [inf] * (n+1)
heap = []
prev = [0]*(n+1)

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))

start,end = map(int,input().split())

def dijkstra(s):
    dist[s] = 0
    heapq.heappush(heap,(0,s))

    while heap:
        weight, now = heapq.heappop(heap)

        if dist[now] < weight:
            continue

        for w, nxt in graph[now]:
            next_w = w + weight 
            if next_w < dist[nxt]:
                dist[nxt] = next_w
                prev[nxt] = now
                heapq.heappush(heap,( next_w, nxt))

    



dijkstra(start)
print(dist[end])

ans = [end]
now = end
while now != start:
    now = prev[now]
    ans.append(now)

ans.reverse()




print(len(ans))
print(*ans)



