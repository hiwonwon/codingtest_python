n = int(input())
ans = [1]*10
for i in range(1,n):
    for j in range(1,10):
        ans[j] += ans[j-1]





print(sum(ans)%10007)