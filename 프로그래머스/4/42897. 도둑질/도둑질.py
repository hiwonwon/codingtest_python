def solution(money):
    answer = 0
    l = len(money)
    #첫번째 원소 고를 때
    dp = [0] * l 
    dp[0] = money[0]
    dp[1] = money[0]
    
    for i in range(2,l-1):
        dp[i] += max(dp[i-1],dp[i-2]+money[i])
    
    #첫번째 원소 안고를 때
    dp2 = [0] * l 
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2,l):
        dp2[i] += max(dp2[i-1],dp2[i-2]+money[i])
        
    answer = max(dp[-2],dp2[-1])
    
    return answer