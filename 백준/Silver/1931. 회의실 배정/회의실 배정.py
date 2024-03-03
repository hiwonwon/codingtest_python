import sys


n = int(input())



meetings = [[0]*2 for _ in range(n)]
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings[i][0] = s
    meetings[i][1] = e

meetings.sort(key = lambda x: (x[1], x[0]))

ans = 0
end_time = 0


# 정렬된 딕셔너리를 사용하여 겹치지 않는 최대 회의 수 계산
for i in range(len(meetings)):
    # 이전 회의 종료시간보다 이후에 진행되는 회의일 경우
    if end_time <= meetings[i][0]:
        ans += 1
        end_time = meetings[i][1]


print(ans)
