import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)


def find(v):
    if parent[v] == v:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a

    if rank[a] == rank[b]:
        rank[a] += 1
    return True


for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')
