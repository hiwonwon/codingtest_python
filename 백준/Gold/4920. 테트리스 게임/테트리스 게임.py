def rotate(arr, n):
        rotated = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[i][j] = arr[n-j-1][i]
        return rotated


def findmax(tetris,n):
    maximum = -99999999
    # -
    
    for i in range(n):
        for j in range(n-3):
            maximum = max(maximum,tetris[i][j]+tetris[i][j+1]+tetris[i][j+2]+tetris[i][j+3])
    
   
    # ㄱㄴ
    for i in range(n-1):
        for j in range(n-2):
            maximum = max(maximum,tetris[i][j]+tetris[i][j+1]+tetris[i+1][j+1]+tetris[i+1][j+2])
    
    #-ㄱ
    for i in range(n-1):
        for j in range(n-2):
            maximum = max(maximum,tetris[i][j]+tetris[i][j+1]+tetris[i][j+2]+tetris[i+1][j+2])
    
    

     # ㅜ
    for i in range(n-1):
        for j in range(n-2):
            maximum = max(maximum,tetris[i][j]+tetris[i+1][j+1]+tetris[i][j+1]+tetris[i][j+2])
    
    #ㅁ
    for i in range(n-1):
        for j in range(n-1):
            maximum = max(maximum,tetris[i][j]+tetris[i][j+1]+tetris[i+1][j+1]+tetris[i+1][j])
    
    return maximum

t = 0
while(True):
    t+=1
    n = int(input())
    if n == 0:
        break
    tetris = [list(map(int,input().split())) for _ in range(n)]
    maximum = findmax(tetris,n)
    tetris = rotate(tetris,n)
    maximum = max(maximum,findmax(tetris,n))
    tetris = rotate(tetris,n)
    maximum = max(maximum,findmax(tetris,n))
    tetris = rotate(tetris,n)
    maximum = max(maximum,findmax(tetris,n))
    print(f"{t}. {maximum}")


