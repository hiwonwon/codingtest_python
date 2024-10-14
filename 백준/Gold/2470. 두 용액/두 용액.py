import itertools
n = int(input())
arr = list(map(int,input().split()))

mini = float('inf')
ans = []
#절대값 순서로 정렬
arr.sort()
start = 0
end = n-1

while(start < end):
    a_start = arr[start]
    a_end = arr[end]

    total = a_start+a_end

    if abs(total) < mini:
        mini = abs(total)
        ans = [a_start,a_end]
    
    if total < 0:
        start +=1
    else:
        end-=1


print(*ans)