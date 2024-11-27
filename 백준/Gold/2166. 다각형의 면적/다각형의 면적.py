n = int(input())
polygon = []
for _ in range(n):
    x,y = map(int, input().split())
    polygon.append([x,y])

ans = 0
#마지막에 n과 1번째 곱하고 빼므로 마지막에 첫번째 것 추가
polygon.append(polygon[0])

for i in range(n):
    ans += polygon[i][0]* polygon[i+1][1] - polygon[i+1][0]*polygon[i][1]

print(abs(ans)/2)