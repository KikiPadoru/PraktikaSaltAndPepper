import re
def is_palindrome(word):
    if (type(word) is not str and type(word) is not int): return False
    word = str(word) if type(word) is int else re.sub(r'[^\w]', '', word).lower()
    for i in range(len(word) // 2 + 1):
        if len(word) < 2: return True
        if word[0] != word[-1]: return False
        word = word[1:-1]


print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))
