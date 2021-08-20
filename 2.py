def coincidence(mass=list(), ranger=range(0)):
    result = list()
    for i in mass:
        if type(i) is float or int and i in ranger:
            result.append(i)

    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
