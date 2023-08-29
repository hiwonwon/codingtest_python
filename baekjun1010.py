t = int(input())
answer = []
for i in range (0,t):
    n, m = map(int, input().split())
    n_r_fac =1

    for j in range(n+1,m+1):
        n_r_fac*=j
    n_minus_r_fac = 1
    for k in range (2,m-n+1):
        n_minus_r_fac*=k
    answer.append(n_r_fac//n_minus_r_fac)

for ans in answer:
    print(ans)
