from itertools import combinations as cb
L, C = map(int, input().split())
arr = sorted(list(input().split()))

for t in cb(arr, L):
    check = False
    cnt = 0
    for c in t:
        if c in ['a', 'e', 'i', 'o', 'u']:
            check = True
        else:
            cnt += 1
    if check == True and cnt >= 2:
        print(''.join(t))