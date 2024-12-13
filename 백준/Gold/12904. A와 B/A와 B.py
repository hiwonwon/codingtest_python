from collections import deque

S = input()
T = input()

queue = deque()
queue.append((T))

while queue:
    cur = queue.popleft()

    if cur == S:
        print(1)
        exit(0)

    if len(cur) > 0 and cur[-1] == 'A':
        queue.append(cur[0:-1])
    elif len(cur) > 0 and cur[-1] == 'B':
        queue.append(cur[0:-1][::-1])

print(0)