def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1,len(arr)):
        pre = arr[i-1]
        if arr[i] != pre:
            answer.append(arr[i])
    return answer