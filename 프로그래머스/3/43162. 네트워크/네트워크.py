def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for c in range(n):
        if visited[c] == False:
            dfs(n,computers,c,visited)
            answer+=1
    return answer

def dfs(n,computers,c,visited):
    visited[c] = True
    for i in range(n):
        #본인이 아닌 컴퓨터와 연결되어 있다면
        if i != c and computers[c][i] == 1:
            #그리고 방문한적 없는 컴퓨터라면
            if visited[i] == False:
                dfs(n,computers,i,visited)
            