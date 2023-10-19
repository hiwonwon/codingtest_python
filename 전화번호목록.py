def solution(phone_book):
    answer = True
    dic = {number:i for  i, number in enumerate(phone_book)}
    
    # print(dic)
    for number in phone_book:  #각 번호 마다 확인
        str_num = ''
        for n in number: # 각 번호를 숫자 하나씩 붙여가며 접두사 존재여부 확인
            str_num += n
            if str_num in dic and str_num != number:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))