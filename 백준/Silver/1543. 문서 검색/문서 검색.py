doc = input()
voca = input()

ans = 0
index = 0
for i in range(len(doc)):
    if index>i:
        continue
    if voca == doc[i:i+len(voca)]:
        ans+=1
        index = i + len(voca)
        
                


print(ans)