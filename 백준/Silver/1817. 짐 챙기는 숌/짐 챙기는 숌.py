n, m = map(int, input().split())



sum = 0
ans = 1
if n != 0:
    input_string = input().split()
    books = [int(char) for char in input_string]
    for i in range(n-1,-1,-1):
        sum+=books[i]

        #한 상자의  최대무게를  넘겼을 때
        if sum > m:
            #해당 책부터 다른 상자에 새로 담음
            sum = books[i]
            ans +=1

    print(ans)
else:
    print(0)