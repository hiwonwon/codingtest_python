S  = input()
bomb = input()
ls = len(S)
lb = len(bomb)

stack = []

for i in range(ls):
    stack.append(S[i])
    #stack의 마지막인덱스부터 폭탄문자열의 길이만큼 확인
    if bomb == ''.join(stack[-lb:]):
        for _ in range(lb):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
