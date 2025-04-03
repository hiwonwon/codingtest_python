import sys

input = sys.stdin.readline

def multiplication(mat_a, mat_b):
    n = len(mat_a)
    rst = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                rst[i][j] += mat_a[i][k] * mat_b[k][j] % 1000    
    return rst

def pow(matrix, n):
    rst = matrix
    if n == 0:
        return rst
    elif n == 1:
        return rst
    elif n % 2:
        y = pow(matrix, (n-1)//2)
        return multiplication(matrix, multiplication(y, y))
    else:
        y = pow(matrix, n//2)
        return multiplication(y, y)
    
n, b = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in pow(matrix, b):
    for j in i:
        print(j%1000, end = ' ')
    print()