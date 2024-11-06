import heapq

n = int(input())
q = []
for _ in range(n):
    s,t = map(int,input().split())
    q.append([s,t])

q.sort()

room = []
heapq.heappush(room,q[0][1])

for i in range(1,n):
    #항상 최솟값과 비교
    if q[i][0] < room[0]:
        heapq.heappush(room,q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room,q[i][1])




print(len(room))