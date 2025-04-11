import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())
M = int(input())
edges = PriorityQueue()
parent = [x for x in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.put((c, a, b))

def find(x):
    
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

edgenum = 0
ans = 0

while edgenum < N-1:
    c, a, b = edges.get()
    
    if find(a) != find(b):
        union(a, b)
        ans += c
        edgenum += 1

print(ans)