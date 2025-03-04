n = int(input())
vocas = []
dic = {}

for _ in range(n):
    tmp = input()
    l = len(tmp)-1
    for j in range(l,-1,-1):
        ch = tmp[l-j]
        if ch not in dic:
            dic[ch] = 10 ** j
        else:
            dic[ch] += 10**j
dic = dict(sorted(dic.items(),key=lambda x:x[1], reverse=True))
num = 9
ans = 0

for alpha in dic:
    #해당 알파벳에 배정된 숫자를 곱해줌
    ans += dic[alpha] * num
    num -=1

print(ans)