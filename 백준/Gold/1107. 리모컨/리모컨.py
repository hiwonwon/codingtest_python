# num_search()
# 고장난 버튼을 제외한 숫자를 조합하여 
# 목표값 target 가장 근사치 값을 찾는다
# return 값 : +,- 버튼 조작횟수를 리턴
# next_num : 검색 시작값
# gap : 증가치 or 감소치
#  gap == 1 : target보다 큰 값 찾는다
#  gap == -1 : target보다 작은 값을 찾는다
def num_search(next_num,gap):
    #증가 버튼을 눌러서 찾는 경우 
    while True:
        # next_num의 각 글자가 nums 집합으로만 이루어지면 bingo
        isvalid=True  
        for i in str(next_num):
            if int(i) not in nums:
                isvalid=False 
                break 
        if isvalid:
            #현재 숫자의 길이 + target값과의 간견(버튼을 누르는 횟수)
            ret=len(str(next_num))+abs(next_num-target)
            #print('>>', next_num)
            break 
        
        next_num=next_num+gap 

        #무한 루프를 방지하기 위한 코드
        #1~9값이 모두 고장나서 0만 입력가능한 경우 
        #target 보다 큰 값은 찾을수 없어서 무한루프 돈다
        #예제 입력6 경우에 해당함
        if next_num > 1000000 or next_num < 0: 
            return 1000000 
    return ret 

#입력
nums=set(list(range(10)))
target=int(input())
n=int(input())
#0이 아니면 고장버튼을 입력받는다
if n!=0:
    gojang=set(list(map(int,input().split())))
    nums=nums-gojang

#조합가능한 큰수에서 -버튼을 누르는 횟수를 구한다. 
ans1=num_search(target, 1)
#조합가능한 작은수에서 +버튼을 누르는 횟수를 구한다.
ans2=num_search(target,-1)
#100번 상태에서 + 또는 - 버튼을 누르는 횟수를 구한다.
ans3=abs(target-100)

#print(ans1,ans2,ans3)
print(min(ans1,ans2,ans3))