import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    visit = [False] * 1_000_001
    max_heap, min_heap= [],[]

    k = int(input())

    for key in range(k):
        order = input().rsplit()

        if order[0] == 'I':
            heapq.heappush(max_heap,(int(order[1])*-1,key))
            heapq.heappush(min_heap, (int(order[1]),key))
            visit[key] = True

        elif order[0] == 'D':
            if order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif order[1] == '-1':
                while min_heap and not visit[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")


                




