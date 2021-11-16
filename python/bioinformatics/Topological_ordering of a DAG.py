def topological_ordering(data):
    file = open(data, 'r')
    my_dict = {}
    key_list = []
    for lines in file:
        lines = lines.rstrip()
        for index in range(0, len(lines)):
            if not lines[index].isdigit(): #ex )10 -> 7,14,15,22
                value = lines[:index] # 10
                key = lines[index+4:].split(',') #7, 14, 15, 22
                key_list.append(value)
                key_list.extend(key)
                for i in key:
                    if i in my_dict:
                        my_dict[i].append(lines[:index])
                    else:
                        my_dict[i] = [lines[:index]]
                break
    key_list = sorted(key_list)
    for item in key_list:
        if not item in my_dict.keys():
            my_dict[item] = []
    # made dictionary with such as ex) 5 : []
    my_list = []
    while len(my_dict) != 0:
        for k in my_dict.keys():
            if my_dict[k] == []:
                my_list.append(k)
        for item in my_list:
            if item in my_dict.keys():
                del my_dict[item]
        for k in my_dict.keys():
            for index in range(0, len(my_dict[k])):
                if my_dict[k][index] in my_list:
                    del my_dict[k][index]
                    break
    my_list = [int(i) for i in my_list]
    return tuple(my_list)
