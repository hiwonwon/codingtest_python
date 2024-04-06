a,b,c = map(int, input().split())

def ans(a,b,c):
    if b == 1:
        return a%c
    else:
        k = ans(a,b//2,c)
        if b%2 == 0 :
            return(k*k%c)
        else:
            return(k*k*a%c)

print(ans(a,b,c))