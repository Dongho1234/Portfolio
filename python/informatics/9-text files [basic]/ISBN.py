'''
Assignment
Write a function display_book_info that takes an ISBN-13 code (str).
If the given ISBN-13 code is valid, the function must print the title,
the authors and the publishers in the format used in the example below.
If the given ISBN-13 code is invalid, and error message must be printed in the format used in the example below.
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

def displayBookInfo(code):
    if isISBN13(code) == False:
        print('Wrong ISBN-13 code')
    import urllib.request
    url = 'http://isbndb.com/api/books.xml?access_key=ZFD8L2Z5&index1=isbn&value1=' + code.strip()
    info = urllib.request.urlopen(url)
    for line in info:
        new_line = line.decode('utf-8').strip()
        if new_line.startswith('<Title>'):
            title = new_line[len('<Title>'):-len('<Title>')-1]
            print('Title: {}'.format(title))
        if new_line.startswith('<AuthorsText>'):
            if ', ' in new_line:
                authors = new_line[len('<AuthorsText>'):-len('<AuthorsText>')-3]
                print('Authors: {}'.format(authors))
            else:
                authors = new_line[len('<AuthorsText>'):-len('<AuthorsText>')-1]
                print('Authors: {}'.format(authors))
        if new_line.startswith('<PublisherText'):
            publisher = new_line[new_line.index('>')+1:-len('</PublisherText>')]
            print('Publisher: {}'.format(publisher))

            
'''
Example
>>> display_book_info('9780136110675')
Title: The Practice of Computing using Python
Authors: William F Punch, Richard Enbody
Publisher: Addison Wesley
>>> display_book_info('9780136110678')
Wrong ISBN-13 code 
'''
