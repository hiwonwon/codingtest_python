
import sys
sys.setrecursionlimit(20000)


def dfs(a,group):
        global check
        if check:
             return
        visited[a] = group
        
        for v in graph[a]:
            #a와 인접한 노드 v가 방문한 적 없다면
            if visited[v] == 0:
                #현재노드와 인접하므로 다른 그룹으로 전달
                dfs(v,-group)
            #인접한 노드가 같은 집합이라면 종료
            elif visited[a] == visited[v]:
                 check = True
                 return

import sys
sys.setrecursionlimit(20000)


def dfs(a,group):
        global check
        if check:
             return
        visited[a] = group
        
        for v in graph[a]:
            #a와 인접한 노드 v가 방문한 적 없다면
            if visited[v] == 0:
                #현재노드와 인접하므로 다른 그룹으로 전달
                dfs(v,-group)
            #인접한 노드가 같은 집합이라면 종료
            elif visited[a] == visited[v]:
                 check = True
                 return
k = int(input())
    

for _ in range(k):
    V,E = map(int,input().split())
    graph = [ [] for _ in range(V+1)]

    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0] * (V+1)
    check = False
    for i in range(1,V+1):
         if visited[i] == 0:
              dfs(i,1)
              if check:
                   break
    if check:
         print("NO")
    else:
         print("YES")
    