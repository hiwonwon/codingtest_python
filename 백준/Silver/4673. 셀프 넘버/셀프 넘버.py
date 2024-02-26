self_list = [i for i in range(1,10001)]


def self_number(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw

#셀프넘버인거 다 체크후 아닌것만 출력 -> 시간에러 ㄱㅊ을까?
for i in range(1,10001):
    if self_number(i) in self_list:
        self_list.remove(self_number(i))


for i in range(len(self_list)):
    print(self_list[i])



