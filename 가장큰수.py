def solution(numbers):
    answer = ''
    numbers = [str(number) for number in numbers]
    numbers.sort(key=lambda num: num*3,reverse=True)

    answer= str(int(''.join(numbers)))


        

    return answer


#import re
# numbers = input()
# numbers = re.findall(r"\d+",numbers)
# numbers = [int(number) for number in numbers]

print(solution([6, 10, 2]))