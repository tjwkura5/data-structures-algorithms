def string_reverse(string):
    reverse_string = ''
    list_chars = list(string)
    list_chars.reverse()
    for char in list_chars:
        reverse_string += char
    
    return reverse_string

print(string_reverse("apple"))
print(string_reverse("John"))
print(string_reverse("phone"))
print(string_reverse("1234567"))

def reverse_words(phrase):
    words = phrase.split(" ")
    new_phrase = ''
    for word in words:
        new_phrase += word + " "
    return new_phrase

print(reverse_words("apple bannana kiwi"))