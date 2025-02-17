n = int(input())
m = int(input())


def union(x,y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    
    return parents[x]




parents = [i for i in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i,j)


ans = "YES"
route = list(map(int,input().split()))
start = parents[route[0]-1]
for i in range(1,m):
    if parents[route[i]-1] != start:
        ans = "NO"
        break


print(ans)