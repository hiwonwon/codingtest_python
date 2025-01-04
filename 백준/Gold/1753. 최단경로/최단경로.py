#다익스트라 기본준비
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
#조건대로 그래프 만들기
v,e = map(int,input().split())
#거리 저장 리스트 만들기
distance = [INF]*(v+1)


start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    u,v,w = map(int,input().split())
    graph[u].append((v,w)) #노드, 비용
    

#다익스트라 실현
def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]) )
    
dijkstra(start)
            
for i in range(1,len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    