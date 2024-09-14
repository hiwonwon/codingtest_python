import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))
coin_list.sort()

dp_table = [0] * (k + 1)
dp_table[0] = 1

for i in coin_list:
    for j in range(i, k+1):
        dp_table[j] += dp_table[j-i]
print(dp_table[k])