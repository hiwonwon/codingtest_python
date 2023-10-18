def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if(citations[i]<=i):
            answer = i
            return answer
    return len(citations)

print(solution([5, 5 ,5 ,5 ,5]))