def solution(s):    
    ls = list(s)
    print(ls[0])
    #소문자라면
    if (ls[0]).islower():
        #대문자로 변환
        ls[0] = (ls[0]).upper()
    
    for i in range(1,len(ls)):
        #이전문자가 공백이고
        if ls[i-1] == ' ':
            #소문자라면
            if (ls[i]).islower():
                #대문자로 변환
                ls[i] = (ls[i]).upper()
        else:
             #eo문자라면
            if (ls[i]).isupper():
                #소문자로 변환
                ls[i] = (ls[i]).lower()
            
                
                
    answer =  ''.join(ls)
    return answer