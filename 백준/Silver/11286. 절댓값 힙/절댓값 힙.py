import heapq
import sys

n =int(input())
q = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not q :
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q,(abs(x),x))