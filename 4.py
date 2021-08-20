def sort_list(mass):
    if len(mass)==0: return mass
    min_m = min(mass)
    max_m = max(mass)
    for i in range(0,len(mass)) :
        if mass[i]==min_m:
            mass[i] = max_m
            continue
        if mass[i]==max_m:
            mass[i] = min_m
    mass.append(min_m)
    return mass

print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
