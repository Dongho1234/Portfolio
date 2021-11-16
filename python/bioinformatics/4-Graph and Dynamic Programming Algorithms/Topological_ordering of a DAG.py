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
'''
>>> topological_ordering('data01.txt')
(1, 4, 5, 2, 3)

>>> topological_ordering('data03.txt')
(1, 11, 28, 3, 41, 47, 50, 53, 59, 61, 62, 68, 70, 71, 48, 69, 16, 35, 66, 0, 29, 12, 25, 
34, 15, 2, 21, 18, 38, 60, 40, 5, 57, 72, 63, 67, 36, 10, 23, 42, 37, 39, 33, 19, 52, 56, 31, 
7, 20, 44, 27, 24, 49, 65, 32, 58, 6, 4, 8, 64, 9, 22, 17, 30, 54, 14, 13, 26, 45, 55, 43, 46, 51)
'''
