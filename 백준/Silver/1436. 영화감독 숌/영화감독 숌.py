n = int(input())

cnt = 0
ans = 0
x = 666

while(cnt<n):
    tmp = x
    isEnd = False

    #해당 숫자의 종말의 수 판별
    while(tmp>=666):
        if tmp % 1000 == 666:
            isEnd=True
        tmp //=10
    #종말의 수라면 cnt 더하고 ans에 넣어주기
    if isEnd:
        cnt+=1
        ans=x
        
    x+=1

print(ans)
