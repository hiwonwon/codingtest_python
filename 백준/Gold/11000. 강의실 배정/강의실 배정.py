import heapq
import sys
N=int(sys.stdin.readline().rstrip())
classes=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
classes.sort()
time_table=[]
heapq.heappush(time_table,classes[0][1])


for i in range(1,N):
    if time_table[0] > classes[i][0]:
        heapq.heappush(time_table,classes[i][1])
    else:
        heapq.heappop(time_table)
        heapq.heappush(time_table,classes[i][1])


print(len(time_table))

   

