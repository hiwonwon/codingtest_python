def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    e=0
    for t in targets:
        if t[0]>=e:
            answer+=1
            e=t[1]
    return answer



import re

# 입력 문자열
input_str = input()

# 숫자를 추출하여 2차원 배열로 저장
numbers = re.findall(r'\d+', input_str)
targets = []

for i in range(0, len(numbers), 2):
    subarray = [int(numbers[i]), int(numbers[i + 1])]
    targets.append(subarray)






print(solution(targets))