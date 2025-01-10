import sys

n, m = map(int, input().split())

# 매트릭스 입력 - 인덱스 에러 방지를 위해 테두리를 0으로 3겹 감싸주기
matrix = []
matrix.append([0] * (m + 6))
matrix.append([0] * (m + 6))
matrix.append([0] * (m + 6))
for _ in range(n):
    matrix.append(
        [0, 0, 0] + list(map(int, sys.stdin.readline().strip().split())) + [0, 0, 0]
    )
matrix.append([0] * (m + 6))
matrix.append([0] * (m + 6))
matrix.append([0] * (m + 6))


# dfs 테트로미노 탐색1  - ㅗ모양군 제외
def search1(count, cur_point, last_x, last_y, prev_move):
    global max_point

    if count == 4:
        max_point = max(max_point, cur_point)
    else:
        if prev_move != "up":
            search1(
                count + 1,
                cur_point + matrix[last_y - 1][last_x],
                last_x,
                last_y - 1,
                "down",
            )
        if prev_move != "down":
            search1(
                count + 1,
                cur_point + matrix[last_y + 1][last_x],
                last_x,
                last_y + 1,
                "up",
            )
        if prev_move != "left":
            search1(
                count + 1,
                cur_point + matrix[last_y][last_x - 1],
                last_x - 1,
                last_y,
                "right",
            )
        if prev_move != "right":
            search1(
                count + 1,
                cur_point + matrix[last_y][last_x + 1],
                last_x + 1,
                last_y,
                "left",
            )


# 테트로미노 탐색2 - ㅗ 모양군 (ㅗ, ㅏ, ㅜ, ㅓ)
def search2(x, y):
    global max_point

    # 기준 블럭의 상/하/좌/우 블럭 중 가장 작은 값을 제거하여 저장
    beside_block_points = [
        matrix[y][x - 1],
        matrix[y + 1][x],
        matrix[y][x + 1],
        matrix[y - 1][x],
    ]
    beside_block_points.remove(min(beside_block_points))

    cur_point = matrix[y][x]
    for block_point in beside_block_points:
        cur_point += block_point
    max_point = max(max_point, cur_point)


# 탐색
max_point = 0
for i in range(3, n + 3):
    for j in range(3, m + 3):
        search1(1, matrix[i][j], j, i, "start!")
        search2(j, i)

# 결과 출력
print(max_point)
