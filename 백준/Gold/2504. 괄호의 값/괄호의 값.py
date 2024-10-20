#2504

def bracket_value(bracket_str):
    result = 0
    stack = []
    substr = ""

    if len(bracket_str) == 0:
        return 1
    
    for i in range(len(bracket_str)):
        if bracket_str[i] == '(' or bracket_str[i] == '[':
            if len(stack) != 0:
                substr = substr + bracket_str[i]
            stack.append(bracket_str[i])
        elif bracket_str[i] == ')':
            if len(stack) > 0:
                pop = stack.pop()
                if pop == '(' and len(stack) == 0:
                    value = bracket_value(substr)
                    if value == 0:
                        return 0
                    result += 2 * value
                    substr = ""
                elif pop == '(' and len(stack) != 0:
                    substr = substr + bracket_str[i]
                else:
                    return 0
            else:
                return 0
        else: # bracket_str[i] == ']'
            if len(stack) > 0:
                pop = stack.pop()
                if pop == '[' and len(stack) == 0:
                    value = bracket_value(substr)
                    if value == 0:
                        return 0
                    result += 3 * value
                    substr = ""
                elif pop == '[' and len(stack) != 0:
                    substr = substr + bracket_str[i]
                else:
                    return 0
            else:
                return 0
        
    if len(stack) != 0:
        return 0
    else:
        return result
    
bracket_str = input()

print(bracket_value(bracket_str))