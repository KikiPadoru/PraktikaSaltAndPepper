import re
def count_words(words):
    words = re.sub(r'[^\w\s+]', '', words).replace('  ',' ').lower().split(' ')
    new_dict = dict()
    for i in words:
        new_dict[i] = new_dict[i]+1 if i in new_dict else 1
    return new_dict

print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
