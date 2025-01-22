n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()


start = 1
end = homes[-1] - homes[0]
ans = 0

while(start <= end):
    mid = (start + end) // 2
    now = homes[0]
    count = 1

    for i in range(1,len(homes)):
        #현재 구한 간격보다 크거나 같은 위치에 있는 집만 세면 현재 간격으로 몇개의 공유기를 설치할 수 있는 알 수 있음
        if homes[i] >= now + mid:
            count += 1
            now = homes[i]
    
    if count >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid -1

print(ans)
