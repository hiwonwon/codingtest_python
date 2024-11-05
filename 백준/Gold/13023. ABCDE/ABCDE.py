n, m = map(int,input().split())

ans = 0
friends = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(x,visited,cnt):
    
    global ans
    
    if cnt == 4:
        ans = 1
        return
    visited[x] = True

    for i in friends[x]:
        if not visited[i]:
            visited[i] = True
            dfs(i,visited,cnt+1)
    visited[x] = False
    

for i in range(n):
    ans = 0
    
    visited =  [False for _ in range(n)]
    dfs(i,visited,0)
    if ans == 1:
        break
        

print(ans)