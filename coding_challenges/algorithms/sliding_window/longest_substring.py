def longest_substring(s):
    length = 0
    window = set()
    L = 0
    for R in range(len(s)):
        while s[R] in window:
            window.remove(s[L])
            L += 1
        window.add(s[R])
        length = max(R-L + 1, length)

    return length

print(longest_substring("pwwwkewp"))