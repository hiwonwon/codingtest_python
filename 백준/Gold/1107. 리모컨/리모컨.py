n = int(input())
m = int(input())
button = [i for i in range(10)]
if m > 0:
    broken = list(map(int, input().split(' ')))
    for b in broken:
        button.remove(b)

def valid(n):
    while n > 0:
        if (n % 10) not in button:
            return False
        n = n // 10
    return True

# 주어진 숫자로 만들 수 있는 n에 가장 가까운 채널
def nearest(n):
    if n < min(button):
        return min(button) - n + 1
    digit = []
    k = n
    while k > 0:
        digit.append(k % 10)
        k = k // 10
    low, high = (0, 0)
    
    # low 구하기
    i = len(digit) - 1
    while i >= 0:
        low = low * 10 + digit[i]
        if digit[i] in button:
            i -= 1
            continue
        else:
            while low > 0:
                low -= 1
                if (low % 10) in button:
                    break
            for j in range(i):
                low = low * 10 + max(button)
            break
    
    # high 구하기
    i = len(digit) - 1
    while i >= 0:
        high = high * 10 + digit[i]
        if digit[i] in button:
            i -= 1
            continue
        else:
            while True:
                high += 1
                if (high % 10) in button:
                    break
            for j in range(i):
                high = high * 10 + min(button)
            break
    
    d = []
    if valid(low):
        d.append((n - low) + len(str(low)))
    if valid(high):
        d.append((high - n) + len(str(high)))
    return min(d)
                  
if button:
    print(min(nearest(n), abs(n - 100)))
else:
    print(abs(n - 100))
