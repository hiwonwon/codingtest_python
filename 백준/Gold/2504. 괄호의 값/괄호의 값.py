from collections import deque
arr = list(input())

stack = []
ans = 0
tmp = 1

for i in range(len(arr)):
    if arr[i] == '(':
        tmp *= 2
        stack.append(arr[i])
    
    elif arr[i] =='[':
        tmp *= 3
        stack.append(arr[i])
    
    elif arr[i] == ']':
        #괄호가 맞지 않을 때
        if not stack or stack[-1]=='(':
            ans =0
            break 
        #쌍이 맞을 때만 더하기
        if arr[i-1] == '[':
            ans += tmp

        tmp //= 3
        stack.pop()

    elif arr[i] == ')':
        #괄호가 맞지 않을 때
        if not stack or stack[-1]=='[':
            ans = 0
            break

        if arr[i-1] == '(':
            ans += tmp


        tmp //= 2
        stack.pop()

    
if stack:
    print(0)
else:
    print(ans)