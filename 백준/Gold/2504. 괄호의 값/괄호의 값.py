def para_check(st):
    para_s = 0
    para_b = 0
    last = []
    right = 1
    for i in range(len(st)):
        if st[i] == '(':
            para_s += 1
            last.append('(')
        elif st[i] == '[':
            para_b += 1
            last.append('[')
        else:
            if st[i]==')':
                if para_s <= 0 or last[-1] != '(':
                    right = 0
                else:
                    para_s -= 1
                    last.pop(-1)
            if st[i]==']':
                if para_b <= 0 or last[-1] != '[':
                    right = 0
                else:
                    para_b -= 1
                    last.pop(-1)
    if para_s != 0 or para_b != 0:
        right = 0
    return right

def para_count(st):
    b = 1
    for j in range(1, len(st)):
        if para_check(st[0:j]) == 1 and para_check(st[j:len(st)]) == 1:
            b = 0
            return 1 + para_count(st[j+1:len(st)])
    if b == 1:
        return b
def para_change(st):
    #print(st)
    if len(st) == 0:
        return 1
    elif st == '()':
        return 2
    elif st == '[]':
        return 3
    if para_count(st) != 1:
        i = 0
        s = 0
        while i < len(st):
            for j in range(i+1, len(st)):
                if para_check(st[i:j+1]) == 1 and (i != 0 or j != len(st)-1):
                    s += para_change(st[i:j+1])
                    i = j + 1
                    break
        return s
    else:
        if st[0] == '(':
            return 2 * para_change(st[1:-1])
        elif st[0] == '[':
            return 3 * para_change(st[1:-1])
st = input()
if para_check(st) == 0:
    print(0)
else:
    print(para_change(st))
            