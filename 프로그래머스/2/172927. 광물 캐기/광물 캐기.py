#다이아, 철, 돌 각각 0~5개
#각 곡괭이는 5개 캔 후 에는 사용 불가
#한번 사용하기 시작한거는 사용할 수 없을때까지, 광물은 주어진 순서대로만 캐야함
#최소한의 피로도는?

#범위가 굉장히 작기때문에 다 확인 가능
#다이아몬드 > 철 > 돌  순으로 좋고
#광물이 돌이올때 돌쓰는게 베스트
def solution(picks, minerals):
    answer = 0
    n = len(minerals)
    
    sum =0
    # 곡괭이의 수를 구한다.
    for i in picks:
        sum += i
    
    #곡괭이로 캘 수 있는 광물만큼 자른다.
    num = sum * 5
    if len(minerals)>sum:
        minerals = minerals[:num]
    
    #광물들을 조사한다.
    cnt_mnls =[[0,0,0] for _ in range((len(minerals) //5 +1))]
    for i in range(len(minerals)):
        if minerals[i]=='diamond':
            cnt_mnls[i//5][0]+=1
        elif minerals[i]=='iron':
            cnt_mnls[i//5][1]+=1
        elif minerals[i]=='stone':
            cnt_mnls[i//5][2]+=1
    
    cnt_mnls.sort(key=lambda x:(-x[0],-x[1],-x[2]))
    
    for cnt_mnl in cnt_mnls:
        dia, iron, stone = cnt_mnl
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                answer += dia + iron + stone
                picks[j] -= 1
                break
            elif picks[j] > 0 and  j == 1:
                picks[j] -= 1
                answer += dia * 5 + iron + stone
                break
            elif picks[j] > 0 and  j == 2:
                picks[j] -= 1
                answer += dia * 25 + iron * 5 + stone
                break
    
    return answer