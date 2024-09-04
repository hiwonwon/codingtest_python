def solution(progresses, speeds):
    answer = []
    stack = []
    
    #각 작업이 며칠 뒤 배포가 가능한지 저장 이때 앞의 작업이 나중에 쌓이도록 역순으로 저장
    for i in range(len(progresses)-1,-1,-1):
        tmp = (100-progresses[i]) // speeds[i]
        if (100-progresses[i]) % speeds[i] != 0:
            tmp += 1
        stack.append(tmp)
        
    day = 0
    while(stack):
        day += 1
        ans = 0
        now = stack.pop()
        #현재 작업이 오늘 날짜에 출시가능하다면
        if now <= day:
            ans += 1
            #뒤의 작업이 남아있을 때
            if stack:
                while(stack):
                    nxt = stack.pop()
                    #뒤의 작업이 오늘 같이 출시 가능할 때
                    if nxt <= day:
                        ans+=1
                    #뒤의 작업이 오늘 출시 불가능 할 때
                    else:
                        stack.append(nxt)
                        break        
            answer.append(ans)
        else:
            stack.append(now)
                
            
    
    return answer