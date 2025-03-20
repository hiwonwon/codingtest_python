import sys
input = sys.stdin.readline

n = int(input())

plus = []
minus = []
zero = False
ans = 0
for _ in range(n):
    tmp = int(input())
    if tmp == 0 :
        zero =True
    elif tmp == 1:
        #1은 바로 더해주기
        ans += 1
    elif tmp >0 :
        plus.append(tmp)
    elif tmp < 0 :
        minus.append(tmp)
    

#절댓값이 큰애들이 앞으로 오도록 
plus.sort(reverse = True)
minus.sort()



for i in range(len(plus)//2):
    ans += plus[i*2]*plus[i*2+1]
if len(plus)%2 == 1:
    ans += plus[-1]


for i in range(len(minus)//2):
    ans += minus[i*2]*minus[i*2+1]
#음수끼리 곱해서 양으로 만들 수 있는 경우 외에 음수가 하나 더있다면
if len(minus)%2 == 1:
    #0이 없다면 하나남은 음의 정수 빼줘야함
    if not zero:
        ans += minus[-1]


print(ans)