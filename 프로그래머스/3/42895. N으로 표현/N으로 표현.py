def solution(N, number):
    answer = 0
    s = [set() for _ in range(8)]
    for i in range (len(s)):
        #N을 i개 사용해서 만든 숫자 s에 삽입
        s[i].add(int(str(N)*(i+1)))
        
    for i in range (len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 !=0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = (i+1)
            #최솟값 구하므로 이후의 값 구하지 않고 break
            break
        else:
            answer = -1
                    
    return answer
                    