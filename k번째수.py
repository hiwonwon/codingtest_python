def solution(array, commands):
    answer = []
    for comand in commands:
        tmp=[]
        start = int(comand[0])-1
        end = int(comand[1])-1
        k =  int(comand[2])-1
        for i in range(end-start+1):
            tmp.append(int(array[i+start]))
        tmp.sort()
        ans = tmp[k]
        answer.append(ans)
    return answer

import re
array = input()
commands= input()

array = re.findall(r'\d+', array)
commands = re.findall(r'\d+',commands)

commands = [[commands[i+j] for j in range(3)]for i in range(0,len(commands),3)]

# print(array)
# for command in commands:

#     print(command)

print(solution(array,commands))