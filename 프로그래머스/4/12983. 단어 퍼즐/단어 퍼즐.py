# strs = 사용가능한 단어조각, t는 만들어야할 문자열
#문장 완성할때 사용하는 단어조각 최솟값?  없으면 -1
#app 쓰는거보다 ap 고르고 ple 고르는게 더 나음 -> 즉 순서대롱 안에 해당되는 젤 긴거 고르면 안된다는거

def solution(strs, t):
    answer = -1
    strs.sort(key=lambda x:len(x))
    dp = [1e9] * len(t) + [0]
    for i in range(len(t)-1,-1,-1):
        #가능한 단어 조각 체크
        for j in range(1,  min(6,len(t)-i+1)):
            if t [i:i+j] in strs:
                dp[i] = min(dp[i],dp[i+j]+1)
    
    if dp[0] != 1e9:
        answer = dp[0]
            
        
    
    return answer