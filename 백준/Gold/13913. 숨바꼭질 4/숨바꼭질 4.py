import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

MAX = 100001

def bfs(start, end):
    visited = [-1] * MAX
    prev = [-1] * MAX  # 경로 추적용

    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        current = queue.popleft()

        if current == end:
            break

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                prev[next_pos] = current
                queue.append(next_pos)

    # 시간 출력
    print(visited[end])

    # 경로 추적
    path = []
    temp = end
    while temp != -1:
        path.append(temp)
        temp = prev[temp]
    path.reverse()

    print(" ".join(map(str, path)))

# 예시 실행
bfs(n, k)