import re
def count_words(words):
    words = re.sub(r'[^\w\s]', '', words)
    words = words.lower()
    print(words)
    new_words = words.split(' ')
    while True:
        try: new_words.remove('')
        except: break
    new_dict = dict()
    for i in new_words:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict
print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
