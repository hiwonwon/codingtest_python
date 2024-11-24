H, W = list(map(int,input().split()))
blocks = list(map(int,input().split()))

ans = 0
for i in range(1, W-1):
    left_max = max(blocks[:i])
    right_max = max(blocks[i+1:])
    ans += max(min(left_max,right_max) - blocks[i], 0)

print(ans)