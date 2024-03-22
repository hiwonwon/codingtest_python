
n = int(input())
i = 0
tmp = 1 + 6 * i

while n > tmp:
    i += 1
    tmp = tmp + 6 * i

print(i+1)