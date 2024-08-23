class Solution(object):
    def mergeAlternately(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
    
        pointer_one = 0
        pointer_two = 0
        result = []

        while pointer_one < n1 or pointer_two < n2:
            if pointer_one < n1:
                result += word1[pointer_one]
                pointer_one += 1
            if pointer_two < n2:
                result += word2[pointer_two]
                pointer_two += 1
        return "".join(result)