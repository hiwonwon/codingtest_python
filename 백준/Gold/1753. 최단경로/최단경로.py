import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[start] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for connect in graph[now]:
            cost = dist + connect[1]
            if cost < distance[connect[0]]:
                distance[connect[0]] = cost
                heapq.heappush(q, (cost, connect[0]))

dijkstra(start)
for i in range(1, n+1):
    print("INF" if distance[i]==INF else distance[i])