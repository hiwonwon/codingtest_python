n = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(n)]

top = [(1, arr[0])]
for i in range(1, n):
    while top and top[-1][1] < arr[i]:
        top.pop()
    if top:     # 더 큰 탑이 존재한다면
        ans[i] = top[-1][0]
    else:       # 현재 제일 큰 탑이라면
        ans[i] = 0
    top.append((i+1, arr[i]))
    
print(*ans)