# from heapq import heappush, heappop, heapify
# from collections import deque
from itertools import combinations
# from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
mis = lambda: map(int, input().split())
INF = float('inf')
# mOD = 10**9 + 7
# sys.setrecursionlimit(10**6)
# dx = [0, 1, -1, 0]
# dy = [1, 0, 0, -1]
# dx = [0, -1, 1, 0, -1, -1, 1, 1]
# dy = [1, 0, 0, -1, 1, -1, 1, -1]

n, m = mis()
city = [[*mis()] for _ in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

def solve(arr):
    ret = 0
    for i in houses:
        dist = INF
        
        for j in arr:
            tmp = abs(i[0] - j[0]) + abs(i[1] - j[1])
            dist = min(dist, tmp)
            
        ret += dist
        
    return ret

ans = INF
for i in combinations(chickens, m):
    distance = solve(i)
    ans = min(ans, distance)

print(ans)