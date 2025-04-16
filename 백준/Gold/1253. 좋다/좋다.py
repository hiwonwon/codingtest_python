import itertools
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0

for i in range(n):
    goal = a[i]
    start = 0
    end = n-1

    while (start < end):
        now = a[start] + a[end]
        if now == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                ans+= 1
                break
        elif now > goal:
            end -= 1
        elif now < goal:
            start += 1
print(ans)