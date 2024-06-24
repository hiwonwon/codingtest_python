import sys
input = sys.stdin.readline

m,n,k = map(int,input().split())
a = [[0]*n for _ in range(m)]
for _ in range(k):
 x1,y1,x2,y2 = map(int,input().split())
 for i in range(y1,y2):
  a[i][x1:x2]=[-1]*(x2-x1)

dy,dx=[1,-1,0,0],[0,0,1,-1]

def dfs(i,j,k):
 if a[i][j]: return
 a[i][j] = k
 stack = [(i,j)]
 cnt = 1
 while stack:
  y,x = stack.pop()
  for i in range(4):
   ny,nx = y+dy[i],x+dx[i]
   if 0<=ny<m and 0<=nx<n and not a[ny][nx]:
    a[ny][nx] = k
    cnt += 1
    stack += [(ny,nx)]
 return cnt

k = 1
ans = []
for i in range(m):
 for j in range(n):
  c = dfs(i,j,k)
  if c:
   ans += [c]
   k += 1

print(k-1)
print(*sorted(ans))