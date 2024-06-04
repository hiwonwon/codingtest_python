N = int(input())

def comb(N):
    base = 1
    base2 = 1
    for i in range(1,10):
        base *= (N+i)
        base2 *= i
    return base//base2
print(comb(N)%10007)

   
