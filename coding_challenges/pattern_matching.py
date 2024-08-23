# Question 2: String Pattern Matching

# You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern. 

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.
# – Where there is a 0 in the pattern, there is a vowel in the substring. 
# – Where there is a 1 in the pattern, there is a consonant in the substring. 

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.


vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def get_sublist(pattern, source):
    string_array = list(source)
    sublists = []
    ending_index = len(pattern)
    for i in range(len(string_array)):
        if ending_index <= len(string_array):
            sublists.append(string_array[i:ending_index])
            ending_index +=1
    
    return sublists

def transform_sublist(pattern, source):
    sublist = get_sublist(pattern, source)
    for list in sublist:
        for i in range(len(list)):
            if list[i] in vowels:
                list[i] = "0"
            else:
                list[i] = "1"
    return sublist

def pattern_match(pattern, source):
    count = 0
    for sub in transform_sublist(pattern, source):
        if list(pattern) == sub:
            count += 1
    return count

def get_pattern_list(source):
    pattern_list = []
    for char in source:
        if char in vowels:
            pattern_list.append("0")
        else:
            pattern_list.append("1")
    return pattern_list

def __pattern_match(pattern, source):
    count = 0
    ending_index = len(pattern)
    pattern_list = get_pattern_list(source)

    for i in range(len(pattern_list)):
        if ending_index > len(pattern_list):
            return count
        else:
            if pattern == ''.join(pattern_list[i:ending_index]):
                count += 1
            ending_index += 1
    


print(__pattern_match("0101", "amazing"))
print(__pattern_match("100", "codesignal"))