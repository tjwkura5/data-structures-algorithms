def is_word_palindrome(word):
    rev = ''.join(reversed(word))
    if rev == word:
        return True
    else:
        return False 

print(is_word_palindrome("malayalam"))