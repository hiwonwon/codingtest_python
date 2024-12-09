#컨베이어: 길이가 n/ 벨트: 2n 
#1 = 올리는 위치 / N= 내리는 위치
#올리는 위치에 올릴때 이동할때 칸의 내구도 1 감소
from collections import deque

ans = 0

n,k = map(int,input().split())
a = deque(map(int,input().split()))
robot = deque([False] * (n))


while (True):
    ans += 1
    
    a.rotate(1)
    robot.rotate(1)

    robot[-1] = 0
    
    #내리는 위치의 전 위치에서부터 확인(가장 먼저 올려진 로봇부터 확인)
    for i in range(n-2,-1,-1):
        #현재 위치에 로봇이 있고 다음위치에 로봇이 없으며 다음 위치의 내구성이 1이상일 때
        if robot[i] and not robot[i+1] and a[i+1] >=1:
            robot[i],robot[i+1] = False, True
            a[i+1] -= 1
    robot[-1] = False
    if a[0] >= 1:
        robot[0] = True
        a[0] -= 1 

    if a.count(0) >= k:
        break

print(ans)

