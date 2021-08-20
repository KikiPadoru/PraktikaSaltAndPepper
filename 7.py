
import enchant


def anagrams(mass,k,word=list(),result=list()):
    if k!=0:
        n_mass = list(mass)
        n_word = list(word)
        for i in range(0,k):
            n_word.append(n_mass.pop(i))
            #print(n_word,' ',n_mass)
            result = anagrams(n_mass,k-1,n_word,result)
            if k==1:
                result.append(''.join(n_word))
                #print(result)
            n_word = list(word)
            n_mass = list(mass)

    return result

def combine_anagrams(mass):
    library = enchant.Dict("en_US")
    for i in range(len(mass)):
        A = list(mass[i])
        result = anagrams(A,len(A))
        new_result =list(set(result))
        #print(result)
        D = list()
        for u in range(len(new_result)):
            if library.check(new_result[u]):
                D.append(new_result[u])
        mass[i] = D
        result.clear()

    return mass


print(combine_anagrams(['cars', "for", "potatoes", "racs", "four", "scar","creams", "scream"]))

