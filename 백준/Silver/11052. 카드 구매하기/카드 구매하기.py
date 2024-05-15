N = int(input())

p = {}
inp = input().split()
for i, elm in enumerate(inp):
    p[i+1] = int(elm)

a = {}

for i in range(1, N+1):
    if i == 1:
        a[1] = p[1]
    elif i == 2:
        a[2] = max(p[2], a[1] + a[1])
    else:
        k = [p[i]]
        for j in range(1, i//2+1):
            k.append(a[j]+a[i-j])
        a[i] = max(k)

print(a[N])
        