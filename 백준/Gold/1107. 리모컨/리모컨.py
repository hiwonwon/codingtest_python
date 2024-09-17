N = int(input())
M = int(input())
buttons = [True for _ in range(10)]
if M != 0:
    impossibles = map(int, input().split())
    for i in impossibles:
        buttons[i] = False
ans = abs(100 - N)
for num in range(1000001):
    num = str(num)
    for el in num:
        if not buttons[int(el)]:
            break
    else:
        ans = min(ans, abs(int(num) - N) + len(num))

print(ans)
