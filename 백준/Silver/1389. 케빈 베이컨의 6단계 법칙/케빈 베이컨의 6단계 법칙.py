import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]

# smallest sum of distances from a "center"


class Node:
    def __init__(self):
        self.val = -1
        self.edges = list()

def f(nodes,x):
    nodes[x].val = 0
    q = [x]
    while len(q) != 0:
        nq = list()
        for i in q:
            for j in nodes[i].edges:
                if nodes[j].val == -1:
                    nq.append(j)
                    nodes[j].val = nodes[i].val+1
        q = nq
    ans = 0
    for ii in range(1,len(nodes)):
        ans += nodes[ii].val
        nodes[ii].val = -1
    return ans

n,m = readints()
nodes = [0]
for _ in range(n):
    nodes.append(Node())
for _ in range(m):
    a,b = readints()
    nodes[a].edges.append(b)
    nodes[b].edges.append(a)

best = 999999999999
ans = -1
for i in range(1,n+1):
    k = f(nodes,i)
    #print(k,i)
    if k < best:
        best = k
        ans = i
print(ans)
