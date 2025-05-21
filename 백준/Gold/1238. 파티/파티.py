import heapq
n, m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,input().split())
    graph[s].append((t,e))

def dijkstra(start):
    dp = [1e9]* (n+1)
    heap = []
    dp[start] = 0
    heapq.heappush(heap,(0,start))
    while(heap):
        wei,now = heapq.heappop(heap)

        if dp[now]< wei:
            continue
        for w, nxt in graph[now]:
            nxt_w = w + wei
            if nxt_w < dp[nxt]:
                dp[nxt] = nxt_w
                heapq.heappush(heap,(nxt_w,nxt))
    return dp
#i 번 도시 -> x번도시
come = dijkstra(x)

#x번 도시 -> i번도시 구하기
back = [0]*(n+1)
for i in range(1,n+1):
    if i!= x:
        tmp = dijkstra(i)
        back[i] = tmp[x]
ans = 0
for i in range(1,n+1):
    
    #i번 도시 -> x번 도시 최단거리 + x번 도시 -> i번 도시 최단거리의 최대값
    ans = max(ans,come[i]+back[i])



print(ans)
