import heapq

n = int(input())
heap = []
for _ in range(n):
    card = int(input())
    heapq.heappush(heap,card)


ans = 0

if len(heap) == 1:
    print(ans)
else:
    while len(heap) > 1:
        #두개 묶음의 합을 구한 후 답에 더해주기
        sum = heapq.heappop(heap) + heapq.heappop(heap)
        ans += sum
        # 묶음의 합과 다음 카드와 비교해야하므로 합을 push
        heapq.heappush(heap,sum)
    print(ans)