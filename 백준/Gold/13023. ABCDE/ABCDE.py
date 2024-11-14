# 그래프 입력 받기
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 체크 배열
visited = [False] * n
found = False  # 경로를 찾았는지 여부를 확인하기 위한 변수

# 깊이가 4인 경로가 있는지 확인하기 위한 함수
def dfs(node, depth):
    global found  # 함수 내에서 경로 찾음 상태를 업데이트할 수 있도록 전역 변수로 설정
    if depth == 4:  # 깊이가 4이면 조건을 만족하는 경로가 있음
        found = True
        return

    # 현재 노드를 방문 처리
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
            if found:  # 경로를 이미 찾았다면 더 이상 탐색하지 않음
                return
    # 방문 상태를 해제 (백트래킹)
    visited[node] = False

# 모든 노드에서 DFS를 시작해보기
for i in range(n):
    dfs(i, 0)
    if found:  # 경로를 찾았다면 반복문 종료
        break

# 결과 출력
print(1 if found else 0)
