from itertools import combinations

l, c = map(int, input().split())

alpha = list(input().split())

mo = ['a','e','i','o','u']
ans = []

for c in combinations(alpha,l):
    c = list(c)
    
    #모음 포함여부 체크
    mcheck = False
    for m in mo:
        if m in c:
            mcheck = True
    cnt = 0
    #자음 개수 체크
    for cc in c:
        if cc not in mo:
            cnt+=1
    
    if mcheck and cnt>= 2:
        c.sort()
        ans.append(c)

answer = []
for a in ans:
    tmp = ''
    for aa in a:
        tmp += aa
    answer.append(tmp)
answer.sort()

for a in answer:
    print(a)