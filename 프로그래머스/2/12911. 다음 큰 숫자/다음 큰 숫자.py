def cnt1(x):
    x = bin(x)
    x = x[2:]
    lx = list(x)
    cnt = lx.count("1")
    return cnt

def solution(n):
    answer = 0
    nn = n+1
    
    while True:
        if cnt1(n) == cnt1(nn):
            answer = nn
            break
        else:
            nn+=1
            
    
    
    return answer