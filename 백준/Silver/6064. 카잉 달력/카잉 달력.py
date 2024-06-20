import sys
input = sys.stdin.readline

def calender(m,n,x,y):
    for i in range(x,m*n+1,m):
        if (i-y)%n==0:
            return i
    return -1

t = int(input().rstrip())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    print(calender(m,n,x,y))