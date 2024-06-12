def solution(s):
    answer = []
    cnt_0 = 0
    cnt_2 = 0
    while(len(s)>1):
        b = len(s)
        s = s.replace('0','')
        a = len(s)
        cnt_0 = cnt_0 + (b-a)
        s = bin(a)
        s = str(s)
        s =s[2:]
        cnt_2+=1
        
    
    answer.append(cnt_2)
    answer.append(cnt_0)
    
    return answer
        