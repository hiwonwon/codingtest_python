import heapq
import os


def main():
    nums = map(int, os.read(0, os.stat(0).st_size).split())
    N = next(nums)
    M = next(nums)
    G = [dict() for _ in range(N + 1)]
    for _ in range(M):
        u = next(nums)
        v = next(nums)
        w = next(nums)
        pw = G[u].get(v, 1 << 29)
        if w < pw:
            G[u][v] = w
    s = next(nums)
    t = next(nums)
    dist = [1 << 29] * (N + 1)
    dist[s] = 0
    p = 2 ** -20
    queue = [0 + s * p]
    while queue:
        i = heapq.heappop(queue)
        du = int(i // 1)
        u = int(i % 1 / p)
        if u == t:
            break
        if du > dist[u]:
            continue
        for v, w in G[u].items():
            dv = du + w
            if dv < dist[v]:
                dist[v] = dv
                heapq.heappush(queue, dv + v * p)
    os.write(1, str(dist[t]).encode())
    os._exit(0)


main()