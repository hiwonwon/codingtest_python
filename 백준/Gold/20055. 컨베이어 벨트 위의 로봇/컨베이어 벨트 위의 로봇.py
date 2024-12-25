import sys


def work():
    global zero_dur

    # 1단계
    n_dur = dur[:]
    n_dur = [n_dur[-1]] + n_dur[:-1]

    for p in range(n - 1, 0, -1):
        robots[p] = robots[p - 1]
    robots[0] = 0
    if robots[-1]:
        robots[-1] = 0

    # 2단계
    for p in range(n - 1, 0, -1):
        if n_dur[p] and robots[p - 1] and not robots[p]:
            robots[p] = robots[p - 1]
            robots[p - 1] = 0
            n_dur[p] -= 1

            if n_dur[p] == 0:
                zero_dur += 1

    if robots[-1]:
        robots[-1] = 0

    # 3단계
    if n_dur[0]:
        robots[0] = 1
        n_dur[0] -= 1
        if n_dur[0] == 0:
            zero_dur += 1

    # 4단계
    if zero_dur >= k:
        return True, n_dur
    return False, n_dur


def check():
    cnt = 0
    for p in range(2 * n):
        if dur[p] == 0:
            cnt += 1

        if cnt >= k:
            return False, cnt
    return True, cnt


n, k = map(int, sys.stdin.readline().split())
dur = list(map(int, sys.stdin.readline().split()))
robots = [0] * n

task = 1
test = check()
if test[0]:
    zero_dur = test[1]
    while True:
        result = work()
        if result[0]:
            break

        dur = result[1][:]
        task += 1

print(task)
