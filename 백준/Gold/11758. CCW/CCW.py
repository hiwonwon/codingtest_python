p1x,p1y = map(int,input().split())
p2x,p2y = map(int,input().split())
p3x,p3y = map(int ,input().split())

x = p1x*p2y + p2x*p3y +p3x*p1y
y = p2x*p1y + p3x*p2y + p1x*p3y

if x-y >0 :
    print(1)
elif x-y == 0:
    print(0)
else:
    print(-1)