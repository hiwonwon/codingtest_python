from collections import deque
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    s = 0
    e = len(people)-1
    
    q = deque(people)

    while(q):
        #남은 사람이 2명이상일때
        if len(q)>=2:
            s = q.popleft()
            e = q.pop()
            
            #두명을 한 보트에 넣는 경우
            if s+e <= limit:
                answer+=1
            #한명만 한 보트에 넣는 경우
            else:
                answer+=1
                q.append(e)
        #남은 사람이 한명일때
        else:
            s = q.popleft()
            answer+=1
    
#     while(s<e):
#         #두 명 담을때
#         if people[s]+people[e] <= limit:
#             s+=1
#             e-=1
#             answer+=1
#         #한명만 담을 때
#         else:
#             s+=1
#             answer+=1
            
#     if len(people)%2 == 1 and s==e:
#         answer+=1
    
    
    return answer