def dfs(start, depth, arr):
    if depth == k - 5:
        combs.append(arr[:])
        return
    
    for i in range(start, len(alph)):
        arr.append(alph[i])
        dfs(i + 1, depth + 1, arr)
        arr.pop()

def word_to_bit(word):
    bit = 0
    for s in word:
        bit |= (1 << ord(s) - ord('a'))
    return bit

n, k = map(int, input().split())
words = [input() for _ in range(n)]
bits = list(map(word_to_bit, words))
base_bit = word_to_bit('antic')

ans = 0
if k >= 5:
    alph = [1 << i for i in range(26) if not base_bit & 1 << i]
    combs = []
    dfs(0, 0, [])

    for comb in combs:
        learned_bit = sum(comb) | base_bit
        cnt = 0
        for bit in bits:
            if bit & learned_bit == bit:
                cnt += 1
        ans = max(ans, cnt)

print(ans)