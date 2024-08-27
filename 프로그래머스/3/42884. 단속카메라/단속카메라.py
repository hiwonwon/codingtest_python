def solution(routes):
    answer = 1
    routes.sort(key = lambda x:[x[0],x[1]])
    start = routes[0][0]
    end = routes[0][1]
    
    for i in range(1,len(routes)):
        #이전 범위와 겹칠때
        if start<= routes[i][0] <= end:
            start = routes[i][0]
            if routes[i][1]< end:
                end = routes[i][1]
            continue
        #새로운 범위가 필요할 때
        else:
            answer+=1
            start = routes[i][0]
            end = routes[i][1]
        
    return answer