n = int(input())
def checkPrime(n):
    if n < 2:                                 
        return False
            
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True

def dfs(x):
    if len(str(x)) == n:
        print(x)
    else:
        for i in range(1,10,2):
            if checkPrime(10*x +i):
                dfs( 10*x+ i)
            else:
                pass

dfs(2)
dfs(3)
dfs(5)
dfs(7)




