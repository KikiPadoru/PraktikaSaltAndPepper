def max_odd(mass=list()):
    result = None
    for i in mass:
        if type(i) is float or type(i) is int and (i % 2 == 1):
            if result == None or result < int(i):
                result = int(i)
    return result

print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
