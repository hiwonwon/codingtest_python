x = int(input())



def func(x):
    res=1
    a=1
    b=1
    row = 1
    if x==1:
        return (a,b)
    while (res<x):
        if row%2==0: #짝수줄
            for  i in range(row-1):
                a+=1
                b-=1
                res+=1
                if(res==x):
                    return (a,b)
                
            #다음줄로 바뀔때
            a+=1
            row+=1
            res+=1
            if(res==x):
                return (a,b)


        else: # 홀수줄
            for  i in range(row-1):
                a-=1
                b+=1
                res+=1
                if(res==x):
                    return (a,b)

            #다음줄로 바뀔때:
            b+=1
            row+=1
            res+=1
            if(res==x):
                return (a,b)


fraction = func(x)
print(f'{fraction[0]}/{fraction[1]}')