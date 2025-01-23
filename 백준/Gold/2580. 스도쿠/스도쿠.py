sdoku = [list(map(int,input().split())) for _ in range(9)]

def row(x,a):
    #해당 행에 n이 이미 있으면 False
    for i in range(9):
        if a == sdoku[x][i]:
            return False
    return True
def col(y,a):
    #해당 열에 n이 이미 있으면 False
    for i in range(9):
        if a == sdoku[i][y]:
            return False
    return True

def square(x,y,a):
    for i in range(3):
        for j in range(3):
            if a == sdoku[x//3*3 + i][y//3*3 + j]:
                return False
    return True

def find(n):
    if n == len(blank):
        for s in sdoku:
            print(*s)
        exit(0)
        
    for i in range(1,10):
        x = blank[n][0]
        y = blank[n][1]

        if row(x,i) and col(y,i) and square(x,y,i):
            sdoku[x][y] = i
            find(n+1)
            sdoku[x][y] = 0 


blank = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append([i,j])
find(0)

