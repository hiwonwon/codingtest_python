import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    s,e = map(int,input().split())
    heapq.heappush(heap,(e,s))

pre_e = 0
ans = 0
while heap:
    e,s = heapq.heappop(heap)
    #이전회의 끝나는 시간이후에 시작되는 회의라면
    if s >= pre_e:
        ans += 1
        pre_e = e

print(ans)


