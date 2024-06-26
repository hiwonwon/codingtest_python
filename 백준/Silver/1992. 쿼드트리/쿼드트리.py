import sys

input=sys.stdin.readline
n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().strip())))

def recur(n,r,c):
    curr=graph[r][c]
    for i in range(r,r+n):
        for j in range(c,c+n):
            if graph[i][j]!=curr:
                print('(',end='')
                recur(n//2,r,c)
                recur(n//2,r,c+n//2)
                recur(n//2,r+n//2,c)
                recur(n//2,r+n//2,c+n//2)
                print(')',end='')
                return
    print(curr,end='')
    return

recur(n,0,0)