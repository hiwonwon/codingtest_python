import sys

sys.setrecursionlimit(10**7)
def find_parent(a):
    global parent_list

    if parent_list[a] == a:
        return a

    parent_list[a] = find_parent(parent_list[a])
    return parent_list[a]

def union(a, b):
    global parent_list
    parent_a = find_parent(a)
    parent_b = find_parent(b)

    if parent_a < parent_b:
        parent_list[parent_b] = parent_a
    else:
        parent_list[parent_a] = parent_b
        
input = sys.stdin.readline

n, m = map(int, input().split())

parent_list = [i for i in range(n+1)]

for _ in range(m):
    operand, a, b = map(int, input().split())

    if operand == 0:
        union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

