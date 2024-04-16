n = int(input())
t = []
for i in range(n):
    t.append(list((input().rstrip())))




ans = []
def devide(x,y,n):
    tmp = t[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if t[i][j] != tmp:
                ans.append("(")
                devide(x,y,n//2)
                devide(x,y+n//2,n//2)
                devide(x+n//2,y,n//2)
                devide(x+n//2,y+n//2,n//2)
                ans.append(")")
                return
    ans.append(tmp)


devide(0,0,n)
print(*ans,sep="")