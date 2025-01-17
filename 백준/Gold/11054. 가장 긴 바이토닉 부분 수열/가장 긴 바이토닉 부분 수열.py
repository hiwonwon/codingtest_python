n = int(input())
a = list(map(int, input().split()))

dp1 = [0] * n
dp2 = [0] * n

for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if a[i] > a[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)
                
for i in range(n-1, -1, -1):
    dp2[i] = 1
    for j in range(n-1, i-1, -1):
        if a[i] > a[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)
            
result = 0
for i in range(n):
    result = max(result, dp1[i]+dp2[i]-1)
print(result)