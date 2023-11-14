s=0
while True:
    n = int(input())
    s+=1
    if n == 0:
        break
    names=[]
    for i in range(n):
        name = input()
        names.append(name)

    unget_dic = {}
    for i in range(2*n-1):
        num, ab = input().split()
        if num in unget_dic:
            del unget_dic[num]
        else:
            unget_dic[num] = ab
    
    unget_st = int(next(iter(unget_dic)))
    print(f"{s} {names[unget_st-1]}")

    