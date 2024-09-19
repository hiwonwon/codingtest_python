from collections import deque
n, k = map(int,input().split())

visited = [0] * 100001

def bfs():
    q = deque()
    q.append(n)

    while(q):
        x = q.popleft()
        if x == k:
            print(visited[x])
            return
        for j in (x-1,x+1,x*2):
            if 0<=j<=100000 and visited[j] == 0:
                if j == 2*x and j != 0:
                    visited[j] = visited[x]
                    q.appendleft(j)
                else:
                    visited[j] = visited[x] + 1
                    q.append(j)

bfs()