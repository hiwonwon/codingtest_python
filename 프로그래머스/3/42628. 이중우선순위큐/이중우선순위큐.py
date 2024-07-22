import heapq

def solution(operations):
    answer = []
    heap = []
    for i in operations:
        if i[0] == "I":
            n = int(i[2:])
            heapq.heappush(heap,n)
        #최솟값 삭제
        if i[0] == "D" and i[2] == "-":
            if len(heap)>0: 
                heapq.heappop(heap)
        #최댓값 삭제
        if i[0] == "D" and i[2] =="1":
            if len(heap)>0:
                mx = max(heap)
                heap.remove(mx)
            
    if len(heap)>0:
        answer.append(max(heap))
        answer.append(heapq.heappop(heap))
    else:
        answer.append(0)
        answer.append(0)

    return answer
