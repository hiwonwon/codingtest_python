n, s = map(int,input().split())
arr = list(map(int,input().split()))

end = 0
inf = float('inf')
ans = inf
count = 0

for i in range(n):

    while count < s and end<n:
        count += arr[end]
        end += 1

    if count >= s:
        ans = min(ans,end-i)
    count -= arr[i]

if ans == inf:
    ans = 0
print(ans)
    
