s1 = input()
s2 = input()

s1 = list(s1)
s2 = list(s2)
lcs = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for j in range(1,len(s2)+1):
    for i in range(1,len(s1)+1):
        if s1[i-1] == s2[j-1]:
            lcs[i][j] =lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])

ans = 0

for l in lcs:
    if max(l) > ans:
        ans = max(l)

print(ans)
