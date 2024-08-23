# Given a string s, partition s such that every 
# substring of the partition is a 
# palindrome .Return all possible palindrome partitioning of s.
# Time: O(n * 2^n), Space: O(n)
def partition(string):
    res = []
    def backtrack(i, curr):
        if i >= len(string):
            if len(curr) > 0 and ''.join(curr) == ''.join(reversed(curr)):
                res.append(''.join(curr))
                return
            else:
                return 
        
        curr.append(string[i])
        backtrack(i+1, curr)

        curr.pop()
   
        backtrack(i+1, curr)

    backtrack(0, [])
    return res

print(partition("aab"))