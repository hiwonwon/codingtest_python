import sys
n, m = map(int,sys.stdin.readline().split())
arr = []

def backT():
    if len(arr) == m:
        print(*arr)
    
    for i in range(1,n+1):
        #중복이 아닐때
        if i not in arr:
            arr.append(i)
            backT()

            arr.pop()

backT()