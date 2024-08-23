def clean_string(phrase):
    clean_string = [s.lower() for s in phrase if s.isalnum()]
    return "".join(clean_string)


def is_palindrome(phrase):
    string = clean_string(phrase)
    L = 0
    R = len(string) -1

    while L < R:
        if string[L] != string[R]:
            return False
        L += 1
        R -= 1
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))

print(is_palindrome("race a car"))

print(is_palindrome(" "))