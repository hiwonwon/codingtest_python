h, w = map(int, input().split())
arr = list(map(int, input().split()))


ans = 0
for i in range(w):
    left_max = max(arr[:i+1])
    right_max = max(arr[i:])

    compare = min(left_max,right_max)
    #벽으로 둘러싸여있고 현재 i번쨰 부분에 물이 고인다면 추가
    if compare > 0 and compare > arr[i]:
        ans += compare - arr[i]





print(ans)