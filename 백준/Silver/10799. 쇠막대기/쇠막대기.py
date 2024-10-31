arr = list(input())

ans = 0
left = 0
for i in range(len(arr)):
    if arr[i] == '(':
        if i+1 < len(arr):
            if arr[i+1] ==')':
                ans += left
            else:
                left+= 1
                
    elif arr[i] == ')':
        if i-1 >= 0:
            if arr[i-1] !='(':
                ans += 1
                left -=1
print(ans)

