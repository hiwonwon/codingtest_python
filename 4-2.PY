n = int(input())

result=0
for i in range(0,n+1):
    if i==3:
        result+=60*60
    else:
        for m in range(0,60):
            for s in range(0,60):
                if m//10 ==3 or m%10 ==3 or s//10==3 or s%10==3:
                    result+=1



print(result)