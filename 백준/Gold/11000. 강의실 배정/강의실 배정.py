""" Solution 1) pq """
# from heapq import heappop, heappush
# import sys
# input = sys.stdin.readline

# pq = [0]
# for s, t in sorted(tuple(map(int, input().split())) for _ in range(int(input()))):
#     heappush(pq, t)
#     if s >= pq[0]: heappop(pq)

# print(len(pq))

""" Solution 2) """
import sys
input = sys.stdin.readline

n = int(input())
st, ed = [], []
for _ in range(n):
    s, t = map(int, input().split())
    st.append(s)
    ed.append(t)
st.sort(); ed.sort()

res = 1
cnt = 0
i = 0
for s in st:
    cnt += 1
    while ed[i] <= s:
        cnt -= 1
        i += 1
    if cnt > res: res = cnt

print(res)