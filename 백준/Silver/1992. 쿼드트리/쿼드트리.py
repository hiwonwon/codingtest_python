size = int(input())
matrix = [list(map(int, input())) for _ in range(size)]

def divide(matrix, size):
    s = 0
    for m in matrix:
        s += sum(m)
    if s == 0:
        return "0"
    if s == size * size:
        return "1"

    size = size // 2
    return (
        "("
        + divide([m[:size] for m in matrix[:size]], size)
        + divide([m[size:] for m in matrix[:size]], size)
        + divide([m[:size] for m in matrix[size:]], size)
        + divide([m[size:] for m in matrix[size:]], size)
        + ")"
    )


print(divide(matrix, size))