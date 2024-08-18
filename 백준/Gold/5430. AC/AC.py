import sys
from collections import deque

def check(command, arr):
    is_reverse = 0 #0 -> 그대로, 1 -> 거꾸로
    for c in command:
        if c == 'R':
            is_reverse = 1 if is_reverse == 0 else 0
        elif c == 'D' and arr:
            arr.popleft() if is_reverse == 0 else arr.pop()
        else:
            return 'error'
    if is_reverse == 0:
        return '[' + ','.join(arr) + ']'
    else:
        return '[' + ','.join(reversed(arr)) + ']'


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    command = sys.stdin.readline().rstrip()
    n = sys.stdin.readline()

    if n == '0\n':
        sys.stdin.readline()
        arr = []
    else:
        arr = sys.stdin.readline().strip("[]\n").split(',')
    
    arr = deque(arr)
    print(check(command, arr))