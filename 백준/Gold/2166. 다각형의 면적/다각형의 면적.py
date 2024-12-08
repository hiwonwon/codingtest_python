import sys

def main():
    import sys
    input = sys.stdin.read().split()
    index = 0
    
    n = int(input[index])
    index += 1
    
    points = []
    for _ in range(n):
        x = int(input[index])
        y = int(input[index + 1])
        points.append((x, y))
        index += 2
    
    # 신발끈 공식 적용
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += (x1 * y2 - y1 * x2)
    
    area = abs(area) / 2.0
    
    # 소수점 아래 둘째 자리에서 반올림하여 첫째 자리까지 출력
    print(f"{area:.1f}")

if __name__ == "__main__":
    main()