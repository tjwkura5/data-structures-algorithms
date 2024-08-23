def createAnagramKey(string):
    key = ''
    for ch in sorted(string):
        key += ch
    return str(key)
    
def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        anagram_key = createAnagramKey(word)
        if anagram_key in anagram_groups:
            anagram_groups[anagram_key].append(word)
        else:
            anagram_groups[anagram_key] = [word]
            
    return list(anagram_groups.values())

def two_string_anagram(string1, string2):
    if createAnagramKey(string1) == createAnagramKey(string2):
        return True
    return False

# canonical = ''.join(sorted(string))



print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""