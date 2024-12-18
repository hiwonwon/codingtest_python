def dfs(start,idx):
    visited[idx] = 1
    nxt = nums[idx]

    if visited[nxt] == 0:
        dfs(start, nxt)
    elif visited[nxt] == 1 and start == nxt:
        ans.append(nxt)



ans = []
n = int(input())
nums = [0]

for i in range(1,n+1):
    b = int(input())
    nums.append(b)


for i in range(1,n+1):
    visited = [0] *(n+1)
    dfs(i,i)
    
print(len(ans))
ans.sort()
for a in ans:
    print(a)