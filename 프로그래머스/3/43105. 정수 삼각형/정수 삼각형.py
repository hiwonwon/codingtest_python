def solution(triangle):
    answer = 0
    n = len(triangle)
    
    for i in range(1,n):
        for j in range(0,len(triangle[i])):
            
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            if j == (len(triangle[i])-1):
                triangle[i][j] += triangle[i-1][j-1]
            if j != 0 and j != (len(triangle[i])-1) : 
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
            
    answer = max(triangle[n-1])
    return answer