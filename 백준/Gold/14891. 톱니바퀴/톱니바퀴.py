def sigye(toapn):
    last= toapn[-1]
    toapn[1:] = toapn[0:7]
    toapn[0] = last
    return toapn

def bansigye(toapn):
    first= toapn[0]
    toapn[0:7] = toapn[1:]
    toapn[-1] = first
    return toapn

toap = []
for i in range(4):
    toap.append(list(input()))

k = int(input())


for _ in range(k):
    n,s = map(int, input().split())
    scheck =[0] *4
    #회전한 톱니바퀴 인덱스에 맞추어 마이너스
    n -= 1
    scheck[n] = s

    #n번째 톱 이전의 톱 돌리기
    for i in range(n-1,-1,-1):
        #맞닿은 극이 반대일 때
        if toap[i+1][6] != toap[i][2]:
            if scheck[i+1] == 1:
                scheck[i] = -1
            if scheck[i+1] == -1:
                scheck[i] = 1
        else:
            #회전이 더이상 없으므로 브레이크
            break
    #n번째 톱 이후의 톱 돌리기
    for i in range(n+1,4):
        #맞닿은 극이 반대일 때
        if toap[i][6] != toap[i-1][2]:
            if scheck[i-1] == 1:
                scheck[i] = -1
            if scheck[i-1] == -1:
                scheck[i] = 1

        else:
            #회전이 더이상 없으므로 브레이크
            break
    #이번 회전에서의 극의 값에 따른 회전여부 저장해서 한번에 회전
    for i in range(4):
        if scheck[i] == 1:
            toap[i] = sigye(toap[i])
        if scheck[i]== -1:
            toap[i] = bansigye(toap[i])
    

ans = 0


for i in range(4):
    if toap[i][0] == "1":
        ans += pow(2,i)
#print(toap)
print(ans)