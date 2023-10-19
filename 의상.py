def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes:
        category = c[1]
        item = c[0]

        if category not in dic: # 키값에 해당 의상종류가 없을 때
            dic[category] = [item]
        else: #이미 해당 의상 종류가 키값에 있을 때
            dic[category].append(item)

    for key,value in dic.items(): # 각 종류별 의상의 수를 곱하면 조합의 수
        answer *= (len(value)+1)
   
    return answer-1 #아무것도 안고르는 경우 제외


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))