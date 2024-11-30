n=int(input())
c=list(map(int,input().split()))
t=[c for i in range(2)]
s=0
for i in range(n-1):
    t[0],t[1]=t[1],list(map(int,input().split()))
    s+=((t[0][0]-c[0])*(t[1][1]-c[1])-(t[1][0]-c[0])*(t[0][1]-c[1]))/2
print(abs(s))