n=int(input("남은돈"))

sum=0 #총 동전의 개수

while (n>=500):
    sum+=int(n/500)
    n=n%500
   

while (n>=100):
   sum+=int(n/100)
   n=n%100

while (n>=50):
    sum+=int(n/50)
    n=n%50

while (n>=10):
    sum+=int(n/10)
    n=n%10

print(sum)