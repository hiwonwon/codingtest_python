def solution(n, info):
    global answer, max_gap
    answer = [-1]
    score = [0] * 11
    max_gap = 0
    
    
    #우승자 여부와 점수차를 반환하는 함수
    def is_winer_gap(score):
        p = 0
        l = 0
        for i in range(11):
            if info[i] >0 or score[i] >0:
                if info[i] >= score[i]:
                    p += 10-i
                else:
                    l += 10-i
        return (l>p, abs(l-p))
    
    def dfs(idx, cnt):
        global max_gap, answer
        
        #모든 점수를 다 확인했거나 화살을 다쐈다면
        if idx == 11 or cnt == 0:
            win,gap = is_winer_gap(score)
            #라이언이 이겼다면
            if win:
                #아직 화살이 남았는데도 이겼다면 남은거 0점에 다 쏴도됨
                if cnt >=0 : 
                    score[10] = cnt
                
                #현재 점수차가 더 크다면 업데이트
                if gap > max_gap:
                    max_gap = gap
                    answer = score.copy()
                    
                elif gap == max_gap:
                    for i in range(11):
                        if answer[i]>0:
                            max_a =i
                        if score[i]>0:
                            max_s= i
                    if max_s>max_a:
                        answer = score.copy()
            return
        
        if cnt > info[idx]:
            #l점에서 라이언이 우승하거나
            score[idx] =info[idx]+1
            dfs(idx+1,cnt-(info[idx]+1))
            #우승하지 않거나
            score[idx] = 0
            
        dfs(idx+1, cnt)
        
            
        
        
    
    
    
    dfs(0,n)
    
    return answer