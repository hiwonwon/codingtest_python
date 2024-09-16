n,k=map(int,input().split())
lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)

def coin_combinations(coins, target):
    dp = [0] * (target + 1)  # 목표 금액만큼 DP 테이블 생성
    dp[0] = 1  # 0원을 만드는 방법은 1가지 (아무 동전도 사용하지 않는 경우)

    for coin in coins:  # 각 동전별로 DP 테이블 갱신
        for j in range(coin, target + 1):  # 동전 금액부터 목표 금액까지 확인
            dp[j] += dp[j - coin]  # dp[j - coin]의 값을 더함
    
    return dp[target]


print(coin_combinations(lst,k))