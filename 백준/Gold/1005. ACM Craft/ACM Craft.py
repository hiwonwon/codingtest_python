#특정 건물을 가장 빨리 지을때까지 걸리는 최소 시간
#k는 순서 규칙
# 즉 건물 건설 순서에 맞게 w를 짓는데 걸리는 최소 시간
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    d = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    degree = [0 for i in range(n+1)]
    dp = [0]*(n+1)
    for _ in range(k):
        x,y = map(int,input().split())
        #y건물을 짓기 이전에 지어야할 건물들 추가
        graph[x].append(y)
        degree[y] += 1

    w = int(input())
    q = deque()
    #위상 0인 건물 먼저 추가
    for i in range(1,n+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = d[i]
    
    while q :
        now = q.popleft()
        for i in graph[now]:
            #위상 -1 해주기
            degree[i] -= 1
            #현재 같은 위상에 있는 요소들을 돌면서 건물을 짓는데 가장 시간이 오래걸리는 애가 dp[i]에 저장됨
            dp[i] = max(dp[i],dp[now]+d[i])
            #현재 확인중인 건물의 위상이 0이되면 다음에 확인하기 위해 q에 넣어줌
            if degree[i] == 0:
                q.append(i)

    print(dp[w])