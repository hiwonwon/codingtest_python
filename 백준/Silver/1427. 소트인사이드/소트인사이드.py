number = input()
array = [digit for digit in number]
sorted_list = sorted(array, reverse=True)

result_string = ''.join(sorted_list)

print(result_string)