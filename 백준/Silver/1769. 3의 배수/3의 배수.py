input_string = input()
x = [int(char) for char in input_string]

ans1 = 0
ans2 = "NO"

y = x
while(len(y)>1):
    temp = sum(y)
    temp = str(temp)
    y = [int(char) for char in temp]
    ans1+=1

if y[0] % 3 == 0:
    ans2 = "YES"
print(ans1)
print(ans2)