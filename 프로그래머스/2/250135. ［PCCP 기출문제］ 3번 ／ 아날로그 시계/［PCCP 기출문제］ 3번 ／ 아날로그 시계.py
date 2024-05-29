def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start = h1*60*60 + m1*60 + s1
    end = h2*60*60 + m2*60 + s2
    
    #0시 또는 12시에 시작하는 경우 미리 계산
    if start == 0 * 3600 or start == 12 * 3600:
        answer += 1
    
    while(start<end):
        
        hcurangle = start / 120 % 360
        mcurangle = start / 10 % 360
        scurangle = start * 6 % 360
        
        # nextangle이 360도가 되면 더작은걸로 간주되는걸 방지하기위한 처리
        hnextangle = 360 if (start+1) / 120 % 360 == 0 else (start+1) / 120 % 360 
        mnextangle = 360 if (start+1) / 10 % 360 == 0 else (start+1) / 10 % 360
        snextangle = 360 if (start+1) * 6 % 360 == 0 else  (start+1) * 6 % 360
        
        
        if scurangle<hcurangle and snextangle >= hnextangle:
            answer+=1
        if scurangle<mcurangle and snextangle >= mnextangle:
            answer+=1
        #시침과 분침이 동일한경우 두번계산됐기 때문에 -1
        if snextangle == hnextangle and hnextangle == mnextangle:
            answer -=1
            
        start +=1
    
    return answer