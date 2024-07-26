def solution(triangle):
    answer = 0
    l = len(triangle)
    for i in range(1,l):
        for j in range(i+1):
            if j == i:
                triangle[i][j] += triangle[i-1][j-1]
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            if 0< j < i:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    
    return max(triangle[l-1])