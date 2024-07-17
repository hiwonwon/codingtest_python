from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip() 
    n = int(input())  
    arr = input().rstrip()[1:-1] 

    if arr:
        arr = deque(arr.split(","))
    else:
        arr = deque()
    
    reverse = False  # 배열의 뒤집힘 상태
    error = False  # 에러 발생 여부

    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if arr:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                error = True
                break
    if error:
        print("error")
    else:
        if reverse:
            arr.reverse()  # 최종적으로 뒤집힌 상태면 뒤집어 줌
        print("[" + ",".join(arr) + "]")