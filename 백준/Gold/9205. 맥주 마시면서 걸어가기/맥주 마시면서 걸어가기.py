import sys
input = sys.stdin.readline

def dist(a, b):
    '''
    a, b는 모두 (x, y) 좌표
    '''
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

T = int(input())
answer = []
for t in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    stores = []
    for _ in range(N):
        stores.append(list(map(int, input().split())))
    dst = list(map(int, input().split()))

    happy_flag = False
    visit = [0 for _ in range(N)]
    stack = [home]
    while stack:
        cur = stack.pop()
        if dist(cur, dst) <= 1000: # 락 페스티벌에 도달 가능?
            answer.append('happy')
            happy_flag = True
            break
        
        for i, store in enumerate(stores):
            if visit[i]:
                continue
            if dist(cur, store) <= 1000:
                stack.append(store)
                visit[i] = 1
    if not happy_flag:
        answer.append('sad')

for t in range(T):
    print(answer[t])