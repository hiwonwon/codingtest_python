num = input()


ans=[0]*10

for i in range(len(num)):
    if(num[i]=="6"or num[i]=="9"):
        if ans[6]<ans[9]:
            ans[6]+=1
        else:
            ans[9]+=1
    else:
        ans[int(num[i])]+=1

print(max(ans))