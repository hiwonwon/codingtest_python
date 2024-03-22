def solution(numbers, target):
    answer = 0
    ans = [0]
    
    
    
    for i in numbers:
        graph = []
        for j in ans:
            graph.append(j-i)
            graph.append(j+i)
        ans = graph
            
    return ans.count(target)