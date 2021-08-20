import re

def is_palindrome(word):
    if(type(word) is int):
        word = str(word)
    if(type(word) is not str):
        return False
    word = re.sub(r'[^\w]', '', word)
    word = word.lower()
    print(word)
    len_word = len(word) // 2
    for i in range(len_word+1):
        if len(word) < 2: return True
        if word[0] != word[-1]: return False
        word = word[1:-1]


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
