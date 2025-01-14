n = int(input())
a = list(map(int,input().split()))

nge = [-1] * n
stack = [0]

for i in range(1,n):
    #stack[-1] = 현재 수 
    while stack and a[stack[-1]] < a[i]:
        nge[stack.pop()] = a[i] #오큰수를 찾았으므로 해당 위치 값 등록
    
    stack.append(i)

print(*nge)