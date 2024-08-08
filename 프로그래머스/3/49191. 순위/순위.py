def solution(n, results):
    answer = 0
    #자신한테 진 사람을 담는 그래프
    graph = [[0]*n for _ in range(n)]

    for a,b in results:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = -1
    
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                #i랑 j가 같거나 이미 정의된 관계라면 패스
                if i==j or graph[i][j] in [1,-1]:
                    continue
                #i가 k를 이겼고 k 가 j를 이겼다면
                if graph[i][k] == graph[k][j] == 1:
                    #i가 j를 이긴 것으로 처리
                    graph[i][j] = 1
                    #패배 한 것도 업데이트
                    graph[j][i] = graph[j][k] = graph[k][i] = -1
                
    print(graph)
    for g in graph:
        if g.count(0) == 1:
            answer += 1
    return answer