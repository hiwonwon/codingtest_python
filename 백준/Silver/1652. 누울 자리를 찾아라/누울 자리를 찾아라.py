

n = int(input())


room = []

# 행의 수에 따라 반복
for _ in range(n):
    row = list(input())  # 각 행의 값 입력
    room.append(row)

ans = 0

ans2= 0

#가로체크
for i in range(n):
    cnt = 0
    cnt2= 0 
    for j in range(n):
        #가로
        if room[i][j] == ".":
            cnt+=1
        else:
            #짐일 경우
            if cnt>=2:
                ans+=1
            cnt = 0
        #세로
        if room[j][i] == ".":
            cnt2+=1
        else:
            #짐일 경우
            if cnt2>=2:
                ans2+=1
            cnt2 = 0
    #벽일 경우
    if cnt>=2:
        ans+=1

     #벽일 경우
    if cnt2>=2:
        ans2+=1




print(ans)




print(ans2)