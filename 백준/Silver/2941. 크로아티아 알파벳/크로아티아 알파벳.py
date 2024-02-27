string = input()

ans = len(string)
#알파벳별로 리스트에 저장후
alpha_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]

#문자열 돌며 두개씩 보고 그 두개가 리스트에 있다면 +1 ,만약 두개가 dz라면 그 다음도 = 인지 확인
#dz= 과 z=이 중복됨

for i in range(len(string)-1):
    s = string[i]+string[i+1]

    if s == "dz" and i+2<len(string):
        s = string[i]+string[i+1]+string[i+2]
    if s in alpha_list:
         ans-=1
         
        #  if s == "z=" and i-1>=0:
        #      ss = string[i-1]+s
        #      if s == "dz=":
        #          ans+=1
        #  if s == "dz=":
        #      ans-=1

print(ans)
    
