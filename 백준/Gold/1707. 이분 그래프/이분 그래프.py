import sys
input=sys.stdin.readline

def bfs(s):
    global flag
    q=[]
    q.append(s)
    visited[s]=1
    
    while q:
        c=q.pop(0)
        for n in adj[c]:
            if not visited[n]:
                q.append(n)
                visited[n]=visited[c]*(-1)
            if visited[n]+visited[c] != 0:
                flag=False
                break
    

for _ in range(int(input())):
    V, E = map(int, input().split())
    adj=[[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    flag=True
    visited=[0]*(V+1)
    for i in range(1, V+1):
        if not visited[i]:
            bfs(i)
            
    print("YES" if flag else "NO")