def solution(n, costs):
    answer = 0
    #비용이 가장 적은애부터 오름차순 정렬->for문돌면서 더해주기만 하면 됨
    costs.sort(key = lambda x: x[2]) 
    link = set([costs[0][0]])
    
    # 모두 연결되기 전까지 반복
    while len(link) != n:
        for v in costs:
            #둘이 연결되어있다면 패스
            if v[0] in link and v[1] in link:
                continue
            #둘 중 하나만 들어있다면 연결
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break
    print(link)
    return answer