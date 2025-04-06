N=int(input())
A=list(map(int, input().split()))

stack=[]
result=[-1]*N

for i in range(N):
    while stack and A[stack[-1]]<A[i]:
        result[stack.pop()]=A[i]
    stack.append(i)
    

print(" ".join(map(str,result)))