def getAns(n, y, width, diagonal1, diagonal2):
    ans = 0
    # 모든 행에 대해서 퀸의 위치가 결정되었을 경우
    if y == n:
        # 해결 가능한 경우의 수를 1 증가시킴
        return 1  # 최적화: ans += 1 대신 바로 1을 반환

    for i in range(n):
        # 해당 위치에 이미 퀸이 있는 경우, 대각선 상에 퀸이 있는 경우 스킵
        if width[i] or diagonal1[i + y] or diagonal2[i - y + n - 1]:
            continue

        # 해당 위치에 퀸을 놓음
        width[i] = diagonal1[i + y] = diagonal2[i - y + n - 1] = True

        # 다음 행으로 이동하여 재귀적으로 해결 가능한 경우의 수 찾기
        ans += getAns(n, y + 1, width, diagonal1, diagonal2)

        # 해당 위치에 놓인 퀸을 제거함
        width[i] = diagonal1[i + y] = diagonal2[i - y + n - 1] = False

    return ans

def solution(n):
    # getAns 함수 호출하여 해결 가능한 경우의 수 찾기
    return getAns(n, 0, [False] * n, [False] * (2 * n - 1), [False] * (2 * n - 1))

# 입력 및 실행
n = int(input())  # n 값을 입력받고 정수로 변환
print(solution(n))  # 가능한 퀸 배치 방법 수 출력
