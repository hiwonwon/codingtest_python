n,m = map(int,input().split())
INF = int(1e9)
dist = [INF] * (n+1)

edges = []

for i in range(m):
    a,b,c = map(int,input().split())
    edges.append([a,b,c])

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now = edges[j][0]
            nxt = edges[j][1]
            time = edges[j][2]
            if dist[now] != INF and dist[nxt] > dist[now] + time:
                dist[nxt] = dist[now] + time
                if i == n-1:
                    return True
    return False

check = bf(1)

if check:
    print("-1")
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])