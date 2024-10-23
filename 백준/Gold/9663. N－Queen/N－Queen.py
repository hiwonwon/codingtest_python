from collections import deque
n = int(input())
ans = 0
arr = [0] * n

def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x]-arr[i]) == abs(x-i):
            return False
    return True

def sol(x):
    global ans
    if x == n:
        ans+=1
        return
    else:
        for i in range(n):
            arr[x] = i
            if check(x):
                sol(x+1)

sol(0)
print(ans)