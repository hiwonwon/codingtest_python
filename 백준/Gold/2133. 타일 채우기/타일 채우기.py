N = int(input())

L = [0] * (N+1)
L[0] = 1
if N > 2:
    L[2] = 3


R = [0] * (N+1)

for i in range(2, N+1):
    if i % 2 == 1:
        continue
    else:
        if i > 2:
            R[i] = L[i-4] * 2 + R[i-2]
        L[i] = L[i-2] * 3 + R[i]

print(L[N])