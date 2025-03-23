from collections import deque

MAX = 100000  # 문제 조건에 맞는 최대 범위 (0부터 MAX까지)
# visited = [False] * (MAX + 1)
# prev = [-1] * (MAX + 1)
from collections import defaultdict

visited = defaultdict(lambda: False)
prev = defaultdict(lambda: False)

def bfs(N, K, visited):
	queue = deque([N])
	
	while queue:
		v = queue.popleft()
		if 0 <= v * 2 <= MAX:
			if not visited[v * 2]:
				queue.append(v * 2)
				visited[v * 2] = True
				prev[v * 2] = v
		if 0 <= v + 1 <= MAX:
			if not visited[v + 1]:
				queue.append(v + 1)
				visited[v + 1] = True
				prev[v + 1] = v
		if 0 <= v - 1 <= MAX:
			if not visited[v - 1]:
				queue.append(v - 1)
				visited[v - 1] = True
				prev[v - 1] = v
		if v * 2 == K or v + 1 == K or v - 1 == K:
			break
	path = [K]
	current = K
	while current != N:
		current = prev[current]
		path.append(current)
	path.reverse()
	print(len(path) - 1)
	print(*path)

N, K = map(int, input().split())

bfs(N, K, visited)
