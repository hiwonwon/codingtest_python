#컨베이어 = n / 벨트 = 2n
# 1~2n-1 -> now + 1 / 2n -> 1 
#1 : 올리는 위치 / n : 내리는 위치
# 로봇 올리는 위치에만 올리고 내리는 위치에서 바로 내림
# 올리는 위치 올릴때, 이동시 내구도 -1
# 이동할 때는 이동할 칸 로봇x + 그 칸 내구도 >= 1
#내구도가 0인 칸 개수 >= k 종료

#정답: 몇번째 단계일 때 종료 됐는가?
from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))

checkRobotsOnA = deque([0]*n)

ans = 0
while True:
    ans += 1
    a.rotate(1)
    #내리는 위치 내리기
    checkRobotsOnA[-1] = 0
    checkRobotsOnA.rotate(1)
    checkRobotsOnA[-1] = 0
    #젤 먼저 올라간 애 붜
    for i in range(n-2,-1,-1):
        if checkRobotsOnA[i+1] == 0 and checkRobotsOnA[i] == 1 and a[i+1] > 0:
            checkRobotsOnA[i+1] = 1
            checkRobotsOnA[i] = 0
            a[i+1] -= 1
    checkRobotsOnA[-1] = 0

    if a[0] != 0 and checkRobotsOnA[0] != 1:
        checkRobotsOnA[0] = 1
        a[0] -= 1
    if a.count(0) >= k:
        break

print(ans)

