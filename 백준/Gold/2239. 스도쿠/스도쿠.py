import sys
input = sys.stdin.readline
sdoku = [list(map(int,input().rstrip())) for _ in range(9)]

def row_check(r,n):
    for col in range(9):
        if sdoku[r][col] == n:
            return False
    return True
def col_check(c,n):
    for row in range(9):
        if sdoku[row][c] == n:
            return False
    return True
def square_check(i,j,n):
    for k in range(3*((i//3)),3*((i//3))+3):
        for x in range(3*((j//3)), 3*((j//3))+3):
            if sdoku[k][x] == n:
                return False
    return True


def backtracking(idx):
    if idx == len(zero):
        for i in range(9):
            for j in range(9):
                print(sdoku[i][j], end="")
            print()
        exit()
    x,y = zero[idx]
    for n in range(1,10):
        if row_check(x,n) and col_check(y,n) and square_check(x,y,n):
            sdoku[x][y] = n
            backtracking(idx+1)
            sdoku[x][y] = 0

zero = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
             zero.append((i,j))
backtracking(0)
             