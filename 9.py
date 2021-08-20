def more_return(my_dict,new_dict):
    for k, v in my_dict.items():
        if(v>9):
            new_dict[k]=v
    return new_dict


def connect_dicts(dict1,dict2):
    a =int()
    b = int()
    for i in dict1.values(): a += i
    for i in dict2.values(): b += i
    new_dict = dict()
    if a>b :
        new_dict = more_return(dict2,new_dict)
        new_dict = more_return(dict1,new_dict)
    else:
        new_dict = more_return(dict1,new_dict)
        new_dict = more_return(dict2, new_dict)
    sorted_dict = {}
    sorted_keys = sorted(new_dict, key=new_dict.get)
    for w in sorted_keys:
        sorted_dict[w] = new_dict[w]

    return sorted_dict

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))
