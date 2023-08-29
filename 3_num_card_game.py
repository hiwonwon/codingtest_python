n, m = map(int, input().split())

result = []
for i in range (n):
    data = list(map(int, input().split( )))
    result.append(data)


min_value = max(min(row) for row in result)
print(min_value)
