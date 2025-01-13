R, C = map(int,input().split())
alp = list(input() for _ in range(R))

V = [0]*128   
V[ord(alp[0][0])] = 1
ans = 1

def move_count(y,x,count):
    global ans
    ans = max(ans,count)
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<R and 0<=nx<C and V[ord(alp[ny][nx])] == 0:
                V[ord(alp[ny][nx])] = 1     
                move_count(ny,nx,count+1)
                V[ord(alp[ny][nx])] = 0

move_count(0,0,1)
print(ans)