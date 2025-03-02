import sys
input = sys.stdin.readline

# 입력받기
R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]

# *인 곳과 S인 곳 큐에 넣기 
# 물이 차는 것이 비버의 이동 보다 먼저이다.
queue = []
for i in range(R) :
    for j in range(C) :
        if matrix[i][j] == '*' :
            queue.append([i, j])
            
for i in range(R) :
    for j in range(C) :
        if matrix[i][j] == 'S' :
            # 고슴도치를 0 으로 변경 (시간 count 하기 위해)
            matrix[i][j] = 0
            queue.append([i, j])
            
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# bfs
def bfs() :
    # 큐가 비기 전까지
    while len(queue) > 0 :
        # r, c 꺼내기
        r, c = queue.pop(0)
        
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            # 경계 안에 있고 
            if (nr >= 0 and nr < R and nc >= 0 and nc < C) :
                # 고슴도치가 D에 도달하는 경우
                if (matrix[r][c] != '*' and matrix[nr][nc] == 'D') :
                    print(matrix[r][c] + 1)
                    exit()
                # 물이 이동하는 경우
                if (matrix[r][c] == '*' and matrix[nr][nc] == '.') :
                    matrix[nr][nc] = '*'
                    queue.append([nr, nc])
                # 고슴도치가 이동하는 경우
                elif (matrix[r][c] != '*' and matrix[nr][nc] == '.') :
                    matrix[nr][nc] = matrix[r][c] + 1
                    queue.append([nr, nc])

bfs()
# 고슴도치가 갈 곳이 없는 경우
print("KAKTUS")