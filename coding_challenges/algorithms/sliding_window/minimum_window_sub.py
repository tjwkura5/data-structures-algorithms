def min_window(s, t):
    if t == "": return ""
    
    countT, window = {}, {}
    for c in t:
        countT[c] = countT.get(c, 0)
    
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    L = 0
    for R in range(len(s)):
        char = s[R]
        window[char] = 1 + window.get(c, 0)
        if window[char] in countT and window[char] == countT[char]:
            have +=1
        while have == need:
            if (R-L +1) < resLen:
                res = [L, R]
                resLen = (R- L + 1)
            window[s[L]] -= 1
            if s[L] in countT and window[s[L]] < countT[s[L]]:
                have -= 1
            L += 1
    L, R = res
    return s[L:R+1] if resLen != float("infinity") else ""