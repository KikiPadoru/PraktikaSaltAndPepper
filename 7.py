
import enchant
#import tracemalloc
#tracemalloc.start()
library = enchant.Dict("en_US")
def anagrams(mass,k,word=list(),result=list()):
    if k!=0:
        n_mass = list(mass)
        n_word = list(word)
        for i in range(0,k):
            n_word.append(n_mass.pop(i))
            #print(n_word,' ',n_mass)
            result = anagrams(n_mass,k-1,n_word,result)
            if k==1:
                w =   ''.join(n_word)
                if library.check(w):
                    result.append(w)
            n_word = list(word)
            n_mass = list(mass)

    return result

def combine_anagrams(mass):
    for i in range(len(mass)):
        A = list(mass[i])
        result = anagrams(A,len(A))
        mass[i]=list(set(result))
        result.clear()
    return mass


print(combine_anagrams(['cars', "for", "potatoes", "racs", "four", "scar","creams", "scream"]))
#print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
