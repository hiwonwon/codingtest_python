n = int(input())
O = [0,0]
z = [list(map(int,input().split())) for _ in range(n)]
z.append(z[0])

ccw1 = 0
ccw2 = 0

a = 0
if n%2 == 0: a = int(n/2)+1

for i in range(n):
    if i < a:
        ccw1 += ((O[0]*z[i][1]) + (z[i][0]*z[i+1][1]) + (z[i][0]*O[1]))-((z[i][0]*O[1]) + (z[i+1][0]*z[i][1]) + (O[0]*z[i+1][1]))
    else:
        ccw2 += ((O[0]*z[i][1]) + (z[i][0]*z[i+1][1]) + (z[i][0]*O[1]))-((z[i][0]*O[1]) + (z[i+1][0]*z[i][1]) + (O[0]*z[i+1][1]))

print(abs(ccw1+ccw2)/2)