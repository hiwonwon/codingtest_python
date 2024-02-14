n = int(input())

ans = 1
start , end = 1,1
total = 0

while end <=n:
    if total <=n:
        if total == n:
            ans+=1
        total+=end
        end+=1
    else:
        total-=start
        start+=1
        


print(ans)