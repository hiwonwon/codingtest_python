
import sys
input = sys.stdin.readline

st, ed = [], []
for _ in range(int(input())):
    s, t = map(int, input().split())
    st.append(s)
    ed.append(t)
st.sort(); ed.sort()

res = 1
cnt = 0
i = 0
for s in st:
    cnt += 1
    while ed[i] <= s:
        cnt -= 1
        i += 1
    if cnt > res: res = cnt

print(res)