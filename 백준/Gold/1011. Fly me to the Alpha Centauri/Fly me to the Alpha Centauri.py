


T = int(input())
for i in range(T):
    x,y = map (int,input().split())
    d = y-x
    # 이동거리
    tmp = 0
    #이동횟수
    cnt = 0
    #반복 횟수
    moving = 0
    i = 0
    while ( tmp < d):
        cnt += 1
        if cnt%2 != 0:
            moving += 1
        tmp+= moving
    print(cnt)