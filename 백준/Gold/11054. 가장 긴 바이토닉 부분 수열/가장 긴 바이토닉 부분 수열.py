import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int,input().split()))
rev_seq = seq[::-1]
inc_dp=[1]*N
dec_dp=[1]*N

for i in range(N):
    for j in range(i):
        if seq[i]>seq[j]:
            inc_dp[i] = max(inc_dp[j]+1, inc_dp[i])
        if rev_seq[i]>rev_seq[j]:
            dec_dp[i] = max(dec_dp[j]+1, dec_dp[i])

result=[0]*N
for i in range(N):
    result[i] = inc_dp[i]+dec_dp[N-i-1]-1
print(max(result))