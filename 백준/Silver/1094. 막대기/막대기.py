x = int(input())

result =0
yacksu=[64,32,16,8,4,2,1]

for i in range(0,len(yacksu)):
    if (x==yacksu[i]):
        result=1
        break
    elif(x>yacksu[i]):
        result+=1
        sum = yacksu[i]
        j=1
        while(x!=sum):
            sum +=yacksu[i+j]
            result+=1
            if(sum>x):
                sum -=yacksu[i+j]
                result-=1
            j+=1
        break

print(result)
    
    



