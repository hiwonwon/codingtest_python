def solution(order):
    answer = 0
    assist = []
    i = 1
    while i<len(order)+1:
        assist.append(i)
        while assist and assist[-1] == order[answer]:
            assist.pop()
            answer+=1
        i+=1
    
    return answer