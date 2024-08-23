# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.


nums_map = {'2':['a', 'b', 'c'], '3':['d','e','f'], '4':['g','h','i'], 
            '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p','q','r','s'], 
            '8':['t','u','v'], '9':['w','x','y','z']}
# Time complexity O(n * 4^n)
def letter_combinations(digits):
    res = []
    def dfs(curStr, index):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        
        for letter in nums_map[digits[index]]:
            dfs(curStr + letter, index+1)
        
    dfs('', 0)
    return res

print(letter_combinations('23'))