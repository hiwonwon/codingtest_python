#n개의 마을에 각 1명씩 n명의 학생
#x번 마을에 모여서 파티 , 마을사이에 m개의 단방향 도로 i번째 길 지날때 Ti시간 소비
#각각학생 최단시간에 오고가기
#가장 많은 시간 소비하는 학생 누구?
#같은도로 안주어지며 모두 x도시왕복가능한 경우만 주어짐

#알고리즘 - 다익스트라?
#각 학생의 x번도시 최단거리로 왕복하는 시간 알아야함
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
back = [0]*(n+1)
#x번 도시 -> i번도시
for i in range(1,n+1):
    tmp = dijkstra(i)
    back[i] = tmp[x]
ans = 0
for i in range(1,n+1):
    ans = max(ans,come[i]+back[i])



print(ans)
