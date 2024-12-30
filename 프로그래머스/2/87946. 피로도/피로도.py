import itertools
def solution(k, dungeons):
    answer = -1
    per = list(itertools.permutations(dungeons,len(dungeons)))
    
    for p in per:
        tmp = k
        cnt = 0
        for pp in p:
            if tmp >= pp[0]:
                cnt += 1
                tmp -= pp[1]
            else:
                break
                
        answer = max(answer,cnt)
    
    return answer