def multiply_numbers(my_object = None):
    if my_object==None:
        return None
    result = list(str(my_object))
    res = 1
    flag = False
    for i in result :
        if i.isdigit():
            flag = True
            res *= int(i)
    if flag: return res
    else: return None

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
