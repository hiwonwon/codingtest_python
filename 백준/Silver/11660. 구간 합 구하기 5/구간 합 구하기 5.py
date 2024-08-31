import copy
n, m = [int(x) for x in input().split()]
nums = [[int(x)for x in input().split()] for _ in range(n)]
coordinates = [[int(x)for x in input().split()] for _ in range(m)]

for i in range(n):
    for j in range(n):
        left = nums[i][j-1] if j > 0 else 0
        top = nums[i-1][j] if i > 0 else 0
        cross = nums[i-1][j-1] if i > 0 and j > 0 else 0
        nums[i][j] += left + top - cross
        

def get_partial_sum(list: list[int]) -> int:
    x1, y1, x2, y2 = list
    raw = nums[x2-1][y2-1]
    left = nums[x2-1][y1-2] if y1-2 > -1 else 0
    top = nums[x1-2][y2-1] if x1-2 > -1 else 0
    cross = nums[x1-2][y1-2] if y1-2 > -1 and x1-2 > -1 else 0
    return nums[x2-1][y2-1] - left - top + cross
    
    
for coordinate in coordinates:
    print(get_partial_sum(coordinate))