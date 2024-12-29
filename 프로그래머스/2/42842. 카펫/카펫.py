def solution(brown, yellow):
    answer = []
    
    x = 0
    y = 0
    for i in range(1,yellow+1):
        #노란색칸에 나누어 떨어지는 수라면
        if yellow % i == 0:
            x = yellow // i
            y = i
            if 2*x + 2*y + 4 == brown:
                answer = [x+2,y+2]
                break
    return answer