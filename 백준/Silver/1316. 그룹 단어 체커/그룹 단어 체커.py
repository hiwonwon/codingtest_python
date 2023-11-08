n = int(input())

words = []
for i in range(n):
    string = input()
    words.append(string)



ans = n

for word in words:
    tmp = []
    isGroup =True
    for j in range(len(word)):
        if j >0:
            if( word[j] in tmp ) and (word[j]!=word[j-1]):
                isGroup = False
                #print(word, word[j])
            tmp.append(word[j])
        else:
            tmp.append(word[j])
    if isGroup == False :
        ans -= 1



print(ans)
