m, n, k = map(int, input().split())

#비어있는 좌표판을 만들어줌
background = [[0]*n for _ in range(m)]

klist=[]
for _ in range(k):
   y1,x1,y2,x2 = map(int, input().split())
   #사각형이 그려지는 부분 체크 해줌
   for i in range(x1,x2):
    for j in range(y1,y2):
      background[i][j] = 1  
#print(background)

from collections import deque
ans = []

def bfs(a,b):
  q = deque()
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  q.append((a,b))
  background[a][b] =1
  cnt = 1
  while(q):
    x,y = q.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0<= nx <m and 0<= ny <n and background[nx][ny] == 0:
        background[nx][ny] = 1
        q.append((nx,ny))
        cnt+=1
  ans.append(cnt)



for i in range(m):
  for j in range(n):
    if background[i][j]==0:
      bfs(i,j)
      

print(len(ans))
ans.sort()
for a in ans:
  print(f'{a} ', end='')



