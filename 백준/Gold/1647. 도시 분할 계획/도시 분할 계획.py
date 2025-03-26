def main():
    import sys
    
    lines = sys.stdin.read().rstrip().splitlines()
    
    N, M = map(int, lines[0].split())
    edges = []
    for i in range(1, M + 1):
        a, b, weight = map(int, lines[i].split())
        edges.append([a, b, weight])
    edges.sort(key=lambda e: e[2], reverse=True)
    
    root = [x for x in range(N + 1)]
    root[0] = 1
    
    def get_root(x):
        nonlocal root
        
        if root[x] != x:
            root[x] = get_root(root[x])
        return root[x]
    
    sum_weight = 0
    connected_components = N
    while connected_components > 2:
        a, b, weight = edges.pop()
        
        root_a = get_root(a)
        root_b = get_root(b)
        if root_a != root_b:
            if root_a < root_b:
                root[root_b] = root_a
            else:
                root[root_a] = root_b
            sum_weight += weight
            connected_components -= 1
    
    sys.stdout.write(str(sum_weight))


if __name__ == '__main__':
    main()