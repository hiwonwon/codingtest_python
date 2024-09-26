import sys
n,m = map(int, input().split())
s = [-1]*(n+1)
ipt = list(map(int, sys.stdin.read().split()))
def find(x):
    if s[x] == -1:
        return x
    s[x] = find(s[x])
    return s[x]
def plus(x,y):
    if find(x)!=find(y):
        s[find(y)] = find(x)
    return
for _ in range(m):
    cal, a, b = ipt[_*3], ipt[_*3+1], ipt[_*3+2]
    if cal == 0:
        plus(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")