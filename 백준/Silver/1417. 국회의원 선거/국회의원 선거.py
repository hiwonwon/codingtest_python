n = int(input())

n_list = []
for i in range(n):
    tmp = int(input())
    n_list.append(tmp)

ans = 0
max_index = 0
for i in range(n):
    if n_list[i]>=n_list[max_index]:
        max_index = i

while (max_index!=0):
    ans+=1
    n_list[max_index] -=1
    n_list[0]+=1
    for i in range(n):
        if n_list[i]>=n_list[max_index]:
            max_index = i

print(ans)