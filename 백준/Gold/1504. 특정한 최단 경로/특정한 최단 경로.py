import heapq

N, E = map(int,input().split())
inf = float("INF")
graph = [[] for i in range(N+1)]

for _ in range(E):
    a,b, c = map(int,input().split())
    #양방향이므로 두번 해줌
    graph[a].append((b,c))
    graph[b].append((a,c))


v1,v2 = map(int,input().split())

def dijkstra(start):
    distance = [inf] * (N+1)
    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0

    while q:
        now, dist  = heapq.heappop(q)
        #이미 처리된 노드는 무시
        if distance[now] < dist:
            continue
        #현재 노드와 인접한 노드 확인
        for next_node,ndist in graph[now]:
            d = dist + ndist
            if d < distance[next_node]:
                distance[next_node] = d
                heapq.heappush(q,(next_node,d))
    
    return distance


ans = min(dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[N],dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[N])

if ans < inf:
    print(ans)
else:
    print(-1)