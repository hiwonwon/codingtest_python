n =int(input())
strings=[]
for i in range(n):
    strings.append(input())
set_lst = set(strings)	## set으로 변환해서 중복값을 제거
strings = list(set_lst)	## 다시 list로 변환
strings.sort()
strings.sort(key = len)


for string in strings:
    print(string)