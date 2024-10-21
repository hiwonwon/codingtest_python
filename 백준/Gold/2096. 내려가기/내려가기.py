import sys

line = int(sys.stdin.readline())
first, second, third = map(int, sys.stdin.readline().split())
last = [[first, first], [second, second], [third, third]] # 젤 위에 값들을 먼저 세팅

for _ in range(line-1):
    a, b, c = map(int, sys.stdin.readline().split())
    temp1 = a + min(last[0][0], last[1][0])
    temp2 = a + max(last[0][1], last[1][1])
    temp3 = b + min(last[0][0], last[1][0], last[2][0])
    temp4 = b + max(last[0][1], last[1][1], last[2][1])
    temp5 = c + min(last[1][0], last[2][0])
    temp6 = c + max(last[1][1], last[2][1])
    last = [[temp1, temp2], [temp3, temp4], [temp5, temp6]]

print(max(last[0][1], last[1][1], last[2][1]), min(last[0][0], last[1][0], last[2][0]))
