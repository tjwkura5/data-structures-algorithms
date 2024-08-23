def is_valid(string):
    stack = []
    p_map = {')':'(', '}':'{', ']':'['}
    for char in string:
        if char in p_map.values():
            stack.append(char)
        else:
            if not stack or p_map[char] != stack.pop():
                return False
   
    return not stack 


print(is_valid('(]'))