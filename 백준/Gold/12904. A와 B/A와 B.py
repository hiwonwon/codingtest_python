s = list(input())
t =list(input())
ans = 0
while(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]

    if str(t) == str(s):
        ans = 1
        break

print(ans)