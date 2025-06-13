import sys
import math

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()
n =int(input())
if n == 1:
    print(0)
    exit()

MAX = 4000000
is_prime = [1 for _ in range(n + 1)]
is_prime[0], is_prime[1] = 0, 0

for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(2, n // i + 1):
            is_prime[i * j] = 0
p =[]
for i in range(2,n+1):
    if is_prime[i]:
        p.append(i)


s = len(p)-1
e = len(p)-1
now_sum = p[-1]
ans = 0

while 0<=s<=e and 0<= e<len(p):
    if now_sum > n:
        now_sum -= p[e]
        e-=1
    else:
        if now_sum == n:
            ans += 1
        s -= 1
        if i<0:
            break
        now_sum += p[s]

print(ans)