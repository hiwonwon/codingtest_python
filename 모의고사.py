def solution(answers):
    answer = []
    st1=[]
    st2 =[]
    st3 =[]

    for i in range(len(answers)):
        st1.append(i%5+1)
        if i%2 == 0:
            st2.append(2)
        else:
            if i % 8 == 1:
                st2.append(1)
            if  i % 8 == 3:
                st2.append(3)
            if  i % 8 == 5:
                st2.append(4)
            if  i % 8 == 7:
                st2.append(5)
        
        if i % 10 == 0 or i % 10 ==1:
            st3.append(3)
        if i % 10 == 2 or i % 10 ==3:
            st3.append(1)
        if i % 10 == 4 or i % 10 ==5:
            st3.append(2)
        if i % 10 == 6 or i % 10 ==7:
            st3.append(4)
        if i % 10 == 8 or i % 10 ==9:
            st3.append(5)
    


    scores = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == st1[i]: #1번학생이 정답에 맞을 때
            scores[0]+=1
        if answers[i] == st2[i]:
            scores[1]+=1
        if answers[i] == st3[i]:
            scores[2]+=1


    for i in range(3):
        if max(scores) == scores[i]: # 최대점수 받은 학생일때 answer에 추가
            answer.append(i+1)
    # print(st1)
    # print(st2)
    # print(st3)
    # print(scores)
    return answer


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([1,1,1,1,1]))