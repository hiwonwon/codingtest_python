def solution(arr):
    answer = -1
    INF = int(1e9)
    maxdp = [[-INF for _ in range(len(arr)//2+1)]for _ in range(len(arr)//2+1)]
    mindp = [[INF for _ in range(len(arr)//2+1)]for _ in range(len(arr)//2+1)]
    
    
    #피연산자 값으로 초기화
    for i in range(len(arr)//2+1):
        maxdp[i][i] = int(arr[i*2])
        mindp[i][i] = int(arr[i*2])
    
    for c in range(1,len(maxdp)):
        for i in range(len(maxdp)-c):
            j = i + c
            for k in range(i,j):
                if arr[k*2 + 1] == "+":
                    maxdp[i][j] = max(maxdp[i][j],maxdp[i][k] + maxdp[k+1][j])
                    mindp[i][j] = min(mindp[i][j],mindp[i][k] + mindp[k+1][j])
                elif arr[k*2 + 1] == "-":
                    maxdp[i][j] = max(maxdp[i][j],maxdp[i][k]-mindp[k+1][j])
                    mindp[i][j] = min(mindp[i][j],mindp[i][k]-maxdp[k+1][j])
                    
    
    return maxdp[0][-1]