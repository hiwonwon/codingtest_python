def solution(tickets):
    answer = []
    tickets.sort(key = lambda x:(x[0],x[1]))
    visited = [False] * len(tickets)
    
    def dfs(pre, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        for idx, ticket in enumerate(tickets):
            if ticket[0] == pre and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False
                
    dfs("ICN",["ICN"])
    return answer[0]