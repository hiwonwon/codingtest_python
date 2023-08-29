n, k = map(int, input().split())
min_value=0
while (n!=1):
    if(n%k==0):
        n=n//k
    else:
        n-=1
    min_value+=1

print(min_value)
