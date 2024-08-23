import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
chicken = []
house = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_city_chicken_distance(selected_chicken):
    return sum(min(get_distance(h, c) for c in selected_chicken) for h in house)

min_distance = float('inf')
for combi in combinations(chicken, M):
    min_distance = min(min_distance, get_city_chicken_distance(combi))

print(min_distance)