import sys; input = sys.stdin.readline

# 향상된 DP 풀이
def main():
    n, k = map(int, input().split())
    k += 1

    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        tmp = {}
        for v_bag, w_bag in bag.items():
            if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
                tmp[nv]=nw
        bag.update(tmp)

    print(max(bag.keys()))

main()