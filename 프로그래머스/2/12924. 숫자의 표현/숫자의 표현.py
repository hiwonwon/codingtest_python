def solution(n):
    #자기자신 1개 미리 계산해줌
    answer = 1
    tmp = 0
    start = 1
    i = 1
    while(i<=n):
        if tmp < n:
            tmp +=i
            i+=1
        elif tmp == n:
            answer+=1
            tmp += i
            i+=1
        elif tmp >n:
            tmp-=start
            start+=1

            
    return answer