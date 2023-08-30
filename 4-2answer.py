n = int(input())

result=0
for i in range(0,n+1):
     for m in range(0,60):
          for s in range(0,60):
                if '3' in str(i)+str(m)+str(s):
                     result+=1



print(result)