

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

belt = deque(list(map(int, input().split())))   # 매번돌리기, 칸별 내구도

ridx = deque()  # 각 로봇들의 현재 인덱스
cur = deque([0]*2*N)   # 각 칸별 로봇 존재 여부

answer = 0

while True:
    answer += 1

    belt.appendleft(belt.pop())     #한칸 회전
    cur.appendleft(cur.pop())

    if cur[N-1] == 1:               # 내리는 칸에 가면 로봇 내리기
        cur[N-1] = 0

    # 회전 후, 각 칸의 로봇 이동 결정
    for i in range(N-2, -1, -1):    # 마지막(내리는칸)은 처리했으니 신경쓰지말기, 들어온순서대로, 위에칸만
        if cur[i] == 1:     # 로봇이 존재하는 경우만 움직이기
            if belt[i+1] >= 1 and cur[i+1] == 0:    # 다음칸에 로봇이없고, 내구도가있으면 움직이기
                cur[i] = 0
                cur[i+1] = 1
                belt[i+1] -= 1

    if cur[N-1] == 1:               # 내리는 칸에 가면 로봇 내리기
        cur[N-1] = 0

    if belt[0] >= 1:
        cur[0] = 1
        belt[0] -= 1

    if belt.count(0) >= K:
        break

print(answer)
