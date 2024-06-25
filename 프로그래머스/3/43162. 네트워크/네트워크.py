
def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def dfs(i):
        visited[i] = True
        
        for j in range(n):
            #아직 방문안한 컴퓨터이며 i번째 컴퓨터와 연결된 컴퓨터 방문
            if visited[j]==False and i != j and computers[i][j] == 1:
                visited[j] = True
                dfs(j)
                
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            answer+=1
        
            
            

    return answer