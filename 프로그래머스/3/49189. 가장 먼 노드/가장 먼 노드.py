from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    #각노드별 길이 저장
    ans = [-1]*(n+1)
    ans[1] = 0
    
    q = deque()
    q.append(1)
    
    while(q):
        now = q.popleft()
        
        for i in graph[now]:
            if ans[i] == -1:
                ans[i] = ans[now] + 1
                q.append(i)
        
    
        
    answer = ans.count(max(ans))
    return answer