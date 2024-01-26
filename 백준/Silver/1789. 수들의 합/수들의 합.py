s = int(input())

sum = 0
ans =0
for i in range(1,s+1):
    sum+=i
    ans+=1
    if sum>s:
        ans-=1
        break

print(ans)