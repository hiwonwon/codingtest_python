import sys

n =int(input())

#한줄만 먼저 입력받고 dp에 저장
nums = list(map(int,input().split()))

maxdp = nums
mindp = nums

for _ in range(n-1):
    nums = list(map(int,input().split()))
    maxdp = [nums[0]+max(maxdp[0],maxdp[1]),nums[1]+max(maxdp[0],maxdp[1],maxdp[2]),nums[2]+max(maxdp[1],maxdp[2])]
    mindp = [nums[0]+min(mindp[0],mindp[1]),nums[1]+min(mindp[0],mindp[1],mindp[2]),nums[2]+min(mindp[1],mindp[2])]


print(max(maxdp),min(mindp))