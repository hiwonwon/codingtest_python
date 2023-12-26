s = input()

i = 0
before = s[0]
cnt_0 = 0
cnt_1 = 0
ans = 0
while i < len(s):
    ##0으로 연속된 숫자들의 개수
    if s[i] == "0":
        while i+1 < len(s) and s[i+1] == "0":
            i+=1

        cnt_0+=1
        i+=1
    ##1으로 연속된 숫자들의 개수
    elif s[i] == "1":
        while i+1 < len(s) and s[i+1] == "1":
            i+=1
        cnt_1+=1
        i+=1
ans = min(cnt_1,cnt_0)
print(ans)