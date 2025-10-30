#매일 출연한 가수의 점수 지금까지의 상위K번째 이내 -> 명예의 전당
#매일 명예의 전당 최하위 점수를 발표함
#매일매일의 최하위 점수 리턴해라
import heapq
def solution(k, score):
    answer = []
    
    today = []
    if k <= len(score):
        for i in range(k):
            heapq.heappush(today,score[i])
            answer.append(today[0])

        for i in range(k,len(score)):
            #지금 점수가 명예의 전당 최하위보다 높다면 바꿔끼기
            if score[i] > today[0]:
                heapq.heappop(today)
                heapq.heappush(today,score[i])

            #오늘의 최하위 점수 추가
            answer.append(today[0])
    else:
        for i in range(len(score)):
            heapq.heappush(today,score[i])
            answer.append(today[0])

            
            
    
    return answer