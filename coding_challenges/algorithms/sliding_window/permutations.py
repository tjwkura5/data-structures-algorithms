def permutations(s1, s2):
    R = len(s1)

    for L in range(len(s2)):
        if ''.join(sorted(s1)) == ''.join(sorted(s2[L:R])):
            return True
        else:
            R += 1
    return False
   
print(permutations("ab", "eidboaoo"))