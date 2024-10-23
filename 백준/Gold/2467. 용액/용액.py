import sys
import itertools

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

left = 0
right = n-1
mini = float('inf')
ans = []

while(left<right):
    total = arr[left]+arr[right]
    if abs(total) < mini:
        mini = abs(total)
        ans = [arr[left],arr[right]]
    #합이 음수라면 음수의 정수가 더 작아져야하므로 left에 +1
    if total < 0:
        left += 1
    #합이 양수라면 양수의 정수가 더 작아져야하므로
    else:
        right -= 1
    
    

print(*ans)