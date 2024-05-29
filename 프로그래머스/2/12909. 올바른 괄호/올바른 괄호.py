def solution(s):
    answer = True
    stack = list(s)
    r = 0
    rcheck = False
    
    while(stack):
        c = stack.pop()
        if c == ')':
            r+=1
            rcheck = True
        if c == '(':
            #이전에 ')'가 나왔었다면
            if rcheck:
                r-=1
                #해당 '('로 인해 더이상 남는 ')'가 없다면
                if r == 0:
                    rcheck = False
                    
            else:
                answer = False
    if r!= 0 :
        answer = False
                    

        
    
    

    return answer