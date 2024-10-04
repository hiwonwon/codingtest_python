import itertools

def sosoo(n):
    if n < 2:                                 
        return False
            
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True
        

def solution(numbers):
    answer = 0
    nums = []
    for n in numbers:
        nums.append(n)
        
    inums = []    
    for i in range(1,len(nums)+1):
        for j in itertools.permutations(nums,i):
            j = list(j)
            #0으로 시작하는 수는 i자리수의 숫자에 해당안됨
            if j[0] != '0':
                strtmp = ''.join(j)
                inums.append(int(strtmp))
    #중복 제거
    inums = list(set(inums))
    for j in inums:
        if sosoo(j):
            answer+=1
    
        
    return answer