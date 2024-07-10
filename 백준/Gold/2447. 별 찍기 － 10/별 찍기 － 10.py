n = int(input())
ans = [['*']*n for _ in range(n)]
# n이 3의 몇승인지 구함
k = 0
tmp = n
while(tmp > 1 ):
    tmp /=3
    k += 1

for l in range(1,k+1):
    sqt = 3**l
    for i in range(n):
        for j in range(n):
            if i % sqt == 0 and j % sqt == 0:
                for x in range(0,sqt//3):
                    for y in range(0,sqt//3):
                        if i+x+sqt//3<n and j+y+sqt//3<n:
                            ans[i+x+sqt//3][j+y+sqt//3] = ' '

for i in range(n):
    for j in range(n):
        print(ans[i][j], end="")
    print()