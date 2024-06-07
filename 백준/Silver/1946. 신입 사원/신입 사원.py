import sys
sys.setrecursionlimit(10000)

# M, N, K = map(int, sys.stdin.readline().split())


a = int(input())

result = []
for i in range(a):
    b = int(input())
    all_li = []
    for j in range(b):
        all_li.append(list(map(int, sys.stdin.readline().split())))
    
    all_li.sort(key=lambda x:(x[0]))
    # print(all_li)
    sum = 0
    t_li = [p[1] for p in all_li]
    minnum = 1000000000000
    for i, t  in enumerate(t_li):

        if minnum < t:
            sum+=1
        
        minnum = min(minnum, t)
    result.append(len(all_li)-sum)

for i in result:
    print(i)
        
    
