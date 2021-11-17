'''
Assignment
Write a function overview that takes a list (list) of strings (str) representing ISBN-13 codes.
The function must print an overview that shows the distribution of the list of ISBN-13 codes over the different registration groups. 
Invalid ISBN-13 codes must be included in the overview under the category Errors. 
Use the names of the registration groups and maintain their order as given in the example below.
Registrations groups for which no ISBN-13 codes occur in the list should also be included in the overview (having 0 occurrences).
'''


def isISBN13(code):
    if not isinstance(code, str):
        return False
    if len(code) != 13:
        return False
    if not code[:12].isdigit():
        return False
    if code[:3] not in {'978', '979'}:
        return False
    total = 0
    total_2 = 0
    for i in code[1:12:2]:
        total += int(i)
    t = 3*total
    for i in code[0:11:2]:
        total_2 += int(i)
    b = (total_2+t) % 10
    total_3 = str((10-b) % 10)
    if code[-1] == total_3:
        return True
    else:
        return False


def overview(codes):
    group = [0, 0, 0, 0, 0, 0, 0, 0]
    for code in codes:
        if not isISBN13(code):
            group[7] += 1
        else:
            if int(code[3]) == 0 or int(code[3]) == 1:
                group[0] += 1
            if int(code[3]) == 2:
                group[1] += 1
            if int(code[3]) == 3:
                group[2] += 1
            if int(code[3]) == 4:
                group[3] += 1
            if int(code[3]) == 5:
                group[4] += 1
            if int(code[3]) == 7:
                group[5] += 1
            if int(code[3]) == 6 or int(code[3]) == 8 or int(code[3]) == 9:
                group[6] += 1
    print('English speaking countries: {}'. format(group[0]))
    print('French speaking countries: {}'.format(group[1]))
    print('German speaking countries: {}'.format(group[2]))
    print('Japan: {}'.format(group[3]))
    print('Russian speaking countries: {}'.format(group[4]))
    print('China: {}'.format(group[5]))
    print('Other countries: {}'.format(group[6]))
    print('Errors: {}'.format(group[7]))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
'''
>>> codes = [
...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
...    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
...    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
...    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
...    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
...    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
...    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
...    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
...    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
...    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
...    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
...    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
...    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
...    '9791853742292', '9781796458336', '9791260591924', '9789367398012' 
... ]
>>> overview(codes)
English speaking countries: 8
French speaking countries: 4
German speaking countries: 6
Japan: 3
Russian speaking countries: 7
China: 8
Other countries: 11
Errors: 9 
'''
