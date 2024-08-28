def solution(n, times):
    answer = 0
    left = 1
    #걸릴 수 있는 최대 시간
    right = max(times) * n
    
    while(left<=right):
        mid = (left+right)//2
        people = 0
        
        for t in times:
            #현재 시간을 mid로 두어 전체 심사관이 몇명 심사했는지를 people에 더해줌
            people += mid//t
            
            #n명을 이미 다 심사 했다면 break
            if people >= n:
                break
        #n명보다 큰데 정답의 범위보다 더 큰 경우도 있으므로 해당경우를 위한 예외처리
        if people >= n:
            answer = mid
            right  = mid-1
        #n명 미만으로 심사했다면 범위를 조정
        else:
            left = mid + 1
                
        
        
    
    return answer