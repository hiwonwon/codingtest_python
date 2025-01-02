import heapq


v, e = map(int, input().split())
k = int(input())
inf = float ("INF")
graph = [[] for _ in range(v+1)]
dp = [inf] * (v+1)
heap = []


def Dijkstra(k):
    dp [k] = 0
    heapq.heappush(heap,(0,k))

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for w,nxt in graph[now]:
            nxt_w = weight + w

            if  nxt_w < dp[nxt]:
                dp[nxt] = nxt_w
                heapq.heappush(heap,(nxt_w,nxt))


for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((w,b))



Dijkstra(k)

for i in range(1,v+1):

    if dp[i] == inf:
        print("INF")
    else:
        print(dp[i])
