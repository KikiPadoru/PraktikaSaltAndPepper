def sort_list(mass):
    if len(mass)!=0:
        min_m = min(mass)
        max_m = max(mass)
        mass = [' ' if e == min_m else e for e in mass]
        mass = [min_m if e == max_m else e for e in mass]
        mass = [max_m if e == ' ' else e for e in mass]
        mass.append(min_m)
    return mass

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
