import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

def DFS(next_node, c):
    color[next_node] = c

    for next in graph[next_node]:
        if color[next] == color[next_node]: return False
        elif color[next] == -1:
            if not DFS(next, (c + 1) % 2):
                return False
        
    return True
        

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [-1 for _ in range(V + 1)]

    is_bipartite = True

    for i in range(1, V + 1):
        if color[i] == -1:
            if not DFS(i, 0):
                is_bipartite = False
                break

    if is_bipartite:
        print("YES")
    else : print("NO")
