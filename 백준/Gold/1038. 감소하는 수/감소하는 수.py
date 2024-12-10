from itertools import combinations
n = int(input())

ans = []

for i in range(1,11):
    #i자리수 숫자 조합 구하기
    for j in combinations(range(10),i):
        num = sorted(list(j), reverse= True)
        ans.append(int("".join(map(str,num))))
ans.sort()
print(ans[n] if len(ans)>n else -1)