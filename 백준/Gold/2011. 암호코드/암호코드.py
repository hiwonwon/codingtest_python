pwd = list(map(int,input()))
len = len(pwd)


if pwd[0] == 0:
    print(0)
else:
    dp = [0] * (len+1)
    dp[0] = 1
    dp[1] = 1
    pwd = [0] + pwd
    for k in range(2,len+1):
        if pwd[k] > 0:
            dp[k] += dp[k-1]
        #두자리 수 넣을 수있다면
        if 10<= pwd[k-1]*10 + pwd[k] <= 26:
            dp[k] += dp[k-2]
        
    print(dp[len]%1000000)