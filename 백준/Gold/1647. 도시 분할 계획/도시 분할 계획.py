import itertools
# 현재 모든집 서로 연결됨 어떤 임의 두집 골라도 연결됨
n, m = map(int,input().split())
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append([a,b,c])

edges.sort(key = lambda x:x[2])

parent = [i for i in range(n+1)]

def find(x):
    if x!= parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

span = []
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        span.append(c)
print(sum(span)-max(span))