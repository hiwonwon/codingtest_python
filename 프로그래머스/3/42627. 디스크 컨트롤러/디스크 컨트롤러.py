import heapq
def solution(jobs):
    answer = 0
    heap = []
    start = -1
    now = 0
    i = 0
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <=now:
                heapq.heappush(heap,(j[1],j[0]))
        
        if len(heap) > 0:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            i+=1
            answer += (now-cur[1])
        else:
            now += 1
    
    return int(answer/len(jobs))