import enchant
library = enchant.Dict("en_US")
def anagrams(mass, k, word=list(), result=list()):
    if k != 0:
        n_mass = list(mass)
        n_word = list(word)
        for i in range(0, k):
            n_word.append(n_mass.pop(i))
            result = anagrams(n_mass, k - 1, n_word, result)
            if k == 1:
                w = ''.join(n_word)
                if library.check(w):
                    result.append(w)
                return result
            n_word = list(word)
            n_mass = list(mass)
    return list(set(result))


def combine_anagrams(mass):
    for i in range(len(mass)):
        mass[i] = sorted(anagrams(list(mass[i]), len(mass[i])))
    return mass


print(combine_anagrams(['cars', "for", "potatoes", "racs", "four", "scar","creams", "scream"]))

