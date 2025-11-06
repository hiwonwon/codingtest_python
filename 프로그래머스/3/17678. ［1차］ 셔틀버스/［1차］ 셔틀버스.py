# 9시부터 n회 t분간격 하나엔 최대 m명
# 대기열에 서있는 사람 태움
# 사무실로 갈 수 있는 가장 늦은 도착시각은? (같은 시각중엔 대기열 맨뒤에 섬)
# 
def solution(n, t, m, timetable):
    answer = 0
    start = 9 * 60
    crew_time = [int(time[:2]) * 60 + int(time[3:]) for time in timetable] 
    crew_time.sort()
    bus_time = [9*60 + t*i  for i in range(n)]
    
    i = 0
    for tm in bus_time:
        cnt = 0
        while cnt < m and i <len(crew_time) and crew_time[i] <= tm:
            i += 1
            cnt += 1
        #먼저온 사람들 다 넣고도 자리가 남았을 경우
        if cnt < m: 
            answer = tm
        else:
            #자리 없으면 마지막 크루보다 1분 도착
            answer = crew_time[i-1] -1
        
            
    answer = str(answer// 60).zfill(2) + ":" +str(answer%60).zfill(2)
    
    return answer