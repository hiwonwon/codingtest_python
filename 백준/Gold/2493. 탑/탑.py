n = int(input())
tower = list(map(int, input().split()))

result = [0] * n
stack = []

for i in range(n):
    while stack and stack[-1][0] < tower[i]:
        stack.pop()
    
    if stack:
        result[i] = stack[-1][1]
    
    stack.append((tower[i], i+1))
        
print(' '.join(map(str, result)))