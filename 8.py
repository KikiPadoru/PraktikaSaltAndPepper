def multiply_numbers(my_object = None):
    if my_object != None and not str(my_object).isdigit():
        result = list(str(my_object))
        res = 1
        for i in result :
            if i.isdigit():
                res *= int(i)
        return res
    return None

print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
