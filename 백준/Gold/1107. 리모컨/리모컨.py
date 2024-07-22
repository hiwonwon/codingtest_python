import sys
input = sys.stdin.readline

n = int(input())
m =int(input())

#고장난 버튼 0개인 경우를고려해서 미리 초기화
btn = []

#고장난 버튼 0개인 경우 고려
if m!= 0:
    btn = list(input().split())

ans = abs(100-n)

for i in range(1000000):
    tmp_list = str(i)
    #고장난 버트포함 여부 체크
    j = 0
    while(j < len(tmp_list)):
        if tmp_list[j] not in btn:
            j+=1
        else:
            break
    #고장난 버튼 포함 안했다면 
    if j == len(tmp_list):
        ans  = min(ans,len(tmp_list)+abs(i-n))


print(ans)