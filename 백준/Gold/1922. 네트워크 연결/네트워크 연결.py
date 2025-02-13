#컴퓨터와 컴퓨터를 직접연결, 모든컴퓨터가 연결되어야함
#연결하는 비용을 최소로
#모두 연결못하는 경우 X

#1.모두를 연결하면서 2. 비용이 최소가 되도록하는 선들을 구하는 것
#알고리즘: N<=1000 이므로 이중 for 문까지 가능,최소신장트리!!!
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b



N = int(input())
M = int(input())

edges = []
for _ in range(M):
    a,b,c = map(int,input().split())
    edges.append([c,a,b])

edges.sort()
parent = [0] * (N+1)
for i in range(1,N+1):
    parent[i] = i
total = 0
for edge in edges:
    price,a,b = edge
    #사이클발생시키지 않는 경우 최소신장트리에 포함
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        total += price

print(total)