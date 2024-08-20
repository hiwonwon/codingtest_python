def dfs(grid, x, y, n, visited):
  
  # 상하좌우 방향설정
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  # 현재 탐색할 위치를 저장하는 stack에 시작점인 (x,y)를 넣어줌
  # color는 시작하는 위치의 색을 저장
  stack = [(x, y)]
  color = grid[x][y]

  while stack: # 스택에 요소가 존재하는 동안 반복함
      x, y = stack.pop() # 스택의 가장 앞 칸을 현재 위치로 설정

      if not visited[x][y]: # 아직 방문 안했나 확인
          visited[x][y] = True # 방문 완료

          # 상하좌우에 붙어있는 칸 확인
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]

              if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color: # 1) (nx, ny) 쌍이 그리드 안에 있나 확인하고, 2) 방문했나 안했나 확인하고 3) 그리드 위치의 색이 시작한 부분의 색이랑 같은지 다른지 확인한다.
                  stack.append((nx, ny)) # 3가지 조건이 전부 성립하면 (nx, ny)를 스택에 추가함
                #이 과정을 스택에 요소가 존재하는 동안 반복수

def location_check(grid): # 같은 색으로 연결된 장소를 파악하는 함수
  n = len(grid)
  visited = [[False] * n for _ in range(n)] # False로 초기화된 nxn 리스트 생성(모든 칸 미방문 상태임)
  count = 0 # 연결되는 구역의 숫자를 계산하는 변수

  # i,j 돌면서 확인
  for i in range(n):
      for j in range(n):
          if not visited[i][j]: # 방문 안한 공간은 dfs 함수를 불러와서 연결된 장소들을 확인함
              dfs(grid, i, j, n, visited)
              count += 1 # 탐색이 끝나면 카운트 하나씩 올려줌

  return count

# 입력 받기
n = int(input())
grid = [list(input().strip()) for _ in range(n)]

# 정상인
normal_people = location_check(grid)

# 적록색약인 = R, G를 같은걸로 처리
for i in range(n):
  for j in range(n):
      if grid[i][j] == 'R':
          grid[i][j] = 'G'

disabled_people = location_check(grid)

print(normal_people, disabled_people)