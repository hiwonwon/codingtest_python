#여러 보조PD가 담당가수 출연순서정함
# 한가수를 여러 보조피디가 담당 가능
#서로 모순 안되면서 전체 가수 순서 구하기
from collections import deque
n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
degree = [0] * (n+1)
ans = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)-2):
        graph[tmp[i+1]].append(tmp[i+2])
        degree[tmp[i+2]] += 1
    q = deque()


for i in range(1,n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    ans.append(now)
    
    for i in graph[now]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

if len(ans) != n:
    print(0)
else:
    for a in ans:
        print(a)


