n,m = map(int,input().split())
arr = list(map(int,input().split()))

#각 나머지의 경우의 수 저장하는 배열
r = [0] * m
pre_sum = 0
for i in range(n):
    pre_sum += arr[i]
    r[pre_sum%m] += 1

ans = r[0]

#나머지의 값이 같은 두 부분합 사이의 구간의 부분합은 M으로 나누어 진다
for i in range(m):
    ans += r[i]*(r[i]-1) // 2

print(ans)