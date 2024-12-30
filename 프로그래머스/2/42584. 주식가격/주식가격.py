from collections import deque
def solution(prices):
    l = len(prices)
    answer = [0] * l
    
    for i in range(l):
        p = prices[i]
        tmp = 0
        for j in range(i+1,l):
            tmp += 1
            if prices[j] < p:
                break
        answer[i] = tmp
                
    
    
    return answer