def letter_combinations(digits):
    res = []
    dig_map = {
     '2':["a", "b", "c"],'3':["d", "e", "f"], 
     '4':["g", "h", "i"],'5':['j', 'k', 'l'],
     '6':['m','n','o'],'7':['q','p', 'r', 's'],
     '8':['t', 'u', 'v'],'9':['w', 'x', 'y', 'z']
     }
    def backtrack(i, curStr):
     if len(curStr) == len(digits):
       res.append(curStr)
       print(res)
       return
     for char in dig_map[digits[i]]:
       backtrack(i+1, curStr + char)
    if digits:
      backtrack(0, '')
    return res 

print(letter_combinations("234"))


