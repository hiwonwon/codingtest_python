from collections import defaultdict, deque

N, K=map(int, input().split())
dq=deque([N])
visit=[float('inf')]*100001
count=[0]*100001
visit[N]=0
count[N]=1
while dq:
    x=dq.popleft()
    for y in [x-1, x+1, 2*x]:
        if 0<=y<=100000 :
            if visit[y]>visit[x]+1:
                visit[y]=visit[x]+1
                count[y]=count[x]
                dq.append(y)
            elif visit[y]==visit[x]+1:
                count[y]+=count[x]
print(visit[K])
print(count[K])