def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left = 1
    right = distance
    rocks.append(distance)
    
    
    while(left <= right):
        mid = (left+right)//2
        delete = 0
        pre = 0
        
        for r in rocks:
            if r-pre < mid:
                delete += 1
                if delete > n:
                    break
            else:
                pre = r         
        
        if delete > n :
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
            
    
    
    return answer