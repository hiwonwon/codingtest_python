n = int(input())
ans = []

def hanoi(n,a,b,c):
    if  n == 1:
        ans.append([a,c])
        return
    hanoi(n-1,a,c,b)
    ans.append([a,c])
    hanoi(n-1,b,a,c)


hanoi(n,1,2,3)
print(len(ans))
for h in ans:
    print(h[0],h[1])