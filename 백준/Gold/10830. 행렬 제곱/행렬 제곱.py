n, b = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

b2 = b // 2

def multi(a,b):
    x = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x[i][j]  += a[i][k] * b[k][j] % 1000
    return x

def square(x,n):
    if n == 1:
        return x
    tmp = square(x, n//2)
    if n %2 == 0:
        return multi(tmp,tmp)
    else:
        return multi(multi(tmp,tmp),x)
ans = square(matrix,b)

for i in range(n):
        for j in range(n):
            ans[i][j] = ans[i][j] % 1000
for a in ans:
    print(*a)