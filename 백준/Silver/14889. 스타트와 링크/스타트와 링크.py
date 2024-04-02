
N = int(input())
s =[]
visited = [0]*N

for i in range(N):
    s.append(list(map(int,input().split())))

def team(l,n):
    global res
    start = 0
    link = 0
    if l == N/2:
        for i in range(N):
            for j in range(N):
                if visited[i] == 0 and visited[j] == 0:
                    start+=s[i][j]
                elif visited[i] != 0 and visited[j]!= 0:
                    link+= s[i][j]
        res = min(res,abs(start-link))    
        return
    for i in range(n,N):
        if visited[i] == 0:
            visited[i] = 1
            team(l+1,i+1)
            visited[i] = 0


res = float('inf')
team(0,0)
print(res)

