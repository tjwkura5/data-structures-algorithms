# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

def characterReplacement(s, k):
    length = 0
    L = 0
    map = {}
    maxf = 0
    for R in range(len(s)):
        map[s[R]] = map.get(s[R], 0) + 1
        maxf = max(maxf, map[s[R]])

        while (R-L + 1) - maxf > k:
            map[s[L]] -= 1
            L += 1

        length = max(length, R-L+1)
    return length

print(characterReplacement("ABAB", 2))