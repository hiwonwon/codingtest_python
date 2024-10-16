from collections import deque
n = int(input())
nodes = list(map(int, input().split()))
d = int(input())

def dfs(d):
    nodes[d] = -10
    for i in range(n):
        #d번 노드를 부모로 가진 자식노드 재귀통해 삭제
        if d == nodes[i]:
            dfs(i)

dfs(d)
ans =0 
for i in range(n):
    if nodes[i] != -10 and i not in nodes:
        ans+=1

print(ans)