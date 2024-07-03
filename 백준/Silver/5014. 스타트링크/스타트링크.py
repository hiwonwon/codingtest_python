from collections import deque
f, s, g, u, d = map(int, input().split())

def bfs(f,s,g,u,d):
    q = deque()
    visited = [0 for _ in range(f+1)]
    visited[s] = 1
    q.append(s)
    while(q):
        s = q.popleft()
        if s == g:
            break
        else:
            for ns in (s + u, s - d):
                if 0< ns <=f and visited[ns] == 0:
                    q.append(ns)
                    visited[ns] = visited[s] + 1

    if s != g:
        print("use the stairs")
    else:
        print(visited[g]-1)

bfs(f,s,g,u,d)