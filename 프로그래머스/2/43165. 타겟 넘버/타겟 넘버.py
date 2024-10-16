def solution(numbers, target):
    answer = 0
    
    leaves = [0]
    
    for num in numbers:
        tmp =[]
        #leaves는 이전의 노드
        for leaf in leaves:
            tmp.append(leaf-num)
            tmp.append(leaf+num)
            
        leaves = tmp
            
    answer = leaves.count(target)        
    
    return answer