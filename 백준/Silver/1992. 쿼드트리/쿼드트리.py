import sys
input = sys.stdin.readline 

def compress(x, y, size):
    initial = matrix[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != initial:
                break
        else:
            continue
        break
    else:
        return str(initial)
    
    half = size // 2
    top_left = compress(x, y, half)
    top_right = compress(x, y + half, half)
    bottom_left = compress(x + half, y, half)
    bottom_right = compress(x + half, y + half, half)
    
    return f"({top_left}{top_right}{bottom_left}{bottom_right})"

N = int(input().strip())
matrix = [input().strip() for _ in range(N)]

result = compress(0, 0, N)
print(result)