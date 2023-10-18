import math

def solution(r1, r2):
    answer = 0

    min_y,max_y = r1,r2

    for i in range(0,r2):
        while r2**2<max_y**2+i**2:
            max_y-=1
        while min_y-1 and r1**2 <=(min_y-1)**2+i**2:
            min_y -=1

        answer+= max_y-min_y+1
    answer=answer*4
    return answer


r1, r2 = map(int,input().split())
print(solution(r1,r2))