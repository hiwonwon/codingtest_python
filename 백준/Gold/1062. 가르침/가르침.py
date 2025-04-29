from itertools import combinations
import sys

n, k = map(int,input().split())

words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
if k < 5 :
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit(0)

learn = [0] * 26
#꼭 배워야하는 5개 글자 처리
for a in ('a', 'c', 'i', 'n', 't'):
    learn[ord(a)-ord('a')] = 1


ans = 0

def dfs(idx,cnt):
    global ans
    
    if cnt == k-5:
        tmp = 0
        for word in words:
            #현재 조합 = 새로배우는 글자 + antatica 알파벳 중에 속하는지 확인
            for a in word:
                if learn[ord(a)-ord('a')] == 0:
                    break
            else:
                #현재 단어에 필요한 알파벳이 현재 조합에 다 있다면 개수 추가
                tmp += 1
        if tmp > ans:
            ans = tmp
        return
    
    for i in range(idx,26):
        if not learn[i]:
            learn[i] = 1
            dfs(i,cnt+1)
            learn[i] = 0
        

dfs(0,0)
print(ans)
