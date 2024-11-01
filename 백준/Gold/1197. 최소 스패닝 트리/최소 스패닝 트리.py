import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

v,e = map(int, input().split())
edges = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
edges.sort(key = lambda x:x[2])


#처음엔 부모가 자기 자신
parent = [i for i in range(v+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a= find_parent(a)
    b = find_parent(b)

    if a<b :
        parent[b] = a
    else:
        parent[a] = b

ans = 0
for a,b,c in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        ans += c
print(ans)