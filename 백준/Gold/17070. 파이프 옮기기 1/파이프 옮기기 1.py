n = int(input())
pipes = [list(map(int,input().split())) for _ in range(n)]


#가로 0 세로 1 대각선 2
def dfs(x,y,state):
    global ans
    if x == n-1 and y == n-1 :
        ans+=1

    #다음 상태가 가로인경우    
    if state==0 or state ==2:
        if y+1<n and pipes[x][y+1] == 0:
            dfs(x,y+1,0)
   
   #다음 상태가 세로인경우    
    if state==1 or state ==2:
        if x+1<n and pipes[x+1][y] == 0:
            dfs(x+1,y,1)
    #다음 상태가 세로인경우    
    if x+1<n and y+1<n:
        if pipes[x+1][y+1] == 0 and pipes[x][y+1] == 0 and pipes[x+1][y] == 0:
            dfs(x+1,y+1,2)
ans = 0

if pipes[n-1][n-1] == 1:
    print(0)
else:
    dfs(0,1,0)
    print(ans)




