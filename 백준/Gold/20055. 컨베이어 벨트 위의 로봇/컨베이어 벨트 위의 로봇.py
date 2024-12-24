import sys
from collections import deque

def main(N,K,A):
    A = deque(A)
    robots = deque([False] * N)

    steps = 0
    while True:
        steps += 1

        # 벨트와 로봇의 회전
        A.rotate(1)
        robots.rotate(1)

        # N 번 컨데이너의 로봇을 내린다.
        robots[N-1] = False

        # 가장 앞에있는 로봇부터 이동
        for i in range(N-2, -1, -1):
            if robots[i] and not robots[i+1] and A[i+1] >= 1:
                robots[i], robots[i+1] = False, True
                A[i+1] -= 1
        
        robots[N-1] = False

        if A[0] != 0:
            robots[0] = True
            A[0] -= 1
        
        if A.count(0) >= K:
            break
    
    return steps


N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
res = main(N,K,A)

print(res)
