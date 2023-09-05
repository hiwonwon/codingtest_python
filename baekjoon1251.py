string = input()

ans = 'z'+string

for i in range(1,len(string)-1):
    for j in range(i+1,len(string)):
        s1 = string[:i][::-1]
        s2 = string[i:j][::-1]
        s3 = string[j:][::-1]
        tmp=s1+s2+s3
        ans = min(ans,tmp)

print(ans)