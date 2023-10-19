def solution(nums):
    
    dic ={integer: 0 for i,integer in enumerate(nums) }
    tmp = (len(dic))

    if tmp>= len(nums)/2:
        return int(len(nums)/2)
    else:
        return tmp


print(solution([3,1,2,3]))