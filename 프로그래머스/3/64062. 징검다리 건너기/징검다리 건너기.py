def solution(stones, k):
    left = 1
    right = 200000000
    
    while(left<=right):
        tmp = stones.copy()
        mid = (left+right)//2
        
        cnt = 0
        for t in tmp:
            #못건너는 다리의 수
            if t - mid<= 0 :
                cnt += 1
            else:
                #연속하는 0의 개수만 세도록 처리
                cnt = 0
            #연속되는 못건너는 다리의 길이가 k를 넘으면 종료
            if cnt >= k:
                break
        #못건너는 다리의 길이가 k보다 길다는건 현재 인원이 건널 수 있는 최대 인원보다 크다는 것
        if cnt >= k :
            right = mid - 1
        if cnt < k:
            left = mid + 1
    return left
                
            
