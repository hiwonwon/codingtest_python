def union(a, b):
    a = find(a)
    b = find(b)
    if a in truep and b in truep:
        return
    if a in truep:
        parent[b] = a
    elif b in truep:
        parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축 수행
    return parent[x]

n, m = map(int, input().split())
truep = list(map(int, input().split()[1:]))
parent = [i for i in range(n+1)]  # 초기화

parties = []
for _ in range(m):
    party = list(map(int, input().split()[1:]))
    parties.append(party)
    for i in range(len(party)-1):
        union(party[i], party[i+1])  # 파티의 모든 사람을 같은 그룹으로 합침

# **경로 압축을 적용하여 parent 배열을 최적화**
for i in range(1, n+1):
    find(i)  # 모든 노드에 대해 `find`를 호출하여 경로 압축 적용

ans = 0
for party in parties:
    for p in party:
        if parent[p] in truep:  # 최종 부모 확인
            break
    else:
        ans += 1
print(ans)
