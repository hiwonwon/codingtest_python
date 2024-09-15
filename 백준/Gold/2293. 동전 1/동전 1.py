n, k = map(int, input().split())

D = [1] + [0] * (k)

for _ in range(n):
    i = int(input())
    for j in range(k):
        if D[j] != 0 and j + i <= k:
            D[j + i] += D[j]

print(D[-1])