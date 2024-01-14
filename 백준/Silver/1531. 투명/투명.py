n, m = map(int, input().split())

image = [[0]*100 for _ in range(100)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1-1,x2):
        for k in range(y1-1,y2):
            image[j-1][k-1]+=1

ans = 0

for i in range(100):
    for j in range(100):
        if image[i][j]>m:
            ans+=1


print(ans)