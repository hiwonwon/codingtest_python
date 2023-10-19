def dfs(numbers, target,cur_sum,cur_idx):
    
    if cur_idx == len(numbers): #재귀함수가 마지막으로 도는 부분
        if cur_sum == target:
            return 1
        else:
            return 0
    else:
        ans = 0
        # print("ans:",ans,"cur_sum:",cur_sum,"cur_idx: ",cur_idx)
        ans += dfs(numbers, target,cur_sum + numbers[cur_idx],cur_idx+1)
        # print("ans:",ans,"cur_sum:",cur_sum,"cur_idx: ",cur_idx)
        ans += dfs(numbers, target,cur_sum - numbers[cur_idx],cur_idx+1)
        
        return ans


def solution(numbers, target):
    answer = 0
    cur_sum =0
    cur_idx=0
    answer=dfs(numbers, target,cur_sum,cur_idx)
  
    return answer

print(solution([1, 1, 1, 1, 1],3))