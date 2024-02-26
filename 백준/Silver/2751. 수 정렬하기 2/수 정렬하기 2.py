n = int(input())

list = []
for i in range(n):
    list.append(int(input()))

for i in sorted(list):
    print(i)