

import sys
sys.setrecursionlimit(111111)
def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    next = graph[x]

    #다음 순서가 방문된 곳이라면
    if visited[next]:
        #이미 방문된 곳이 사이클안에 있다면
        if next in cycle:
            #사이클을 이루는 부분부터 결과에 추가
            result += cycle[cycle.index(next):]
        return
    else:
        #다음 순서가 아직 방문된 곳 아니라면 계속 진행
        dfs(next)



T = int(input())
for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int,input().split()))
    result = []
    visited = [True] + [False] * n
    for i in range(1,n+1):
       if not visited[i]:
           cycle = []
           dfs(i)
    print(n-len(result))