t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    lmin = 11
    lmax = 0
    ans = "YES"
    for i in range(n):
        num = input()
        nums.append(num)
    nums.sort()
    ans = "YES"
    for i in range(n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            ans = "NO"
            break
    print(ans)
