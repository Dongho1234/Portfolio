'''
Assignment

Dr. James Bender mentions this secret language on December 31, 1944 in one of his articles in New York Times Magazine. 
Reportedly, the spoken language is used by English children to talk secretly about things that are not intended for the ears of adults.

To translate a message into Turkey Irish, all you have to do is insert ab before each sequence of consecutive vowels. 
However, if the sequence of vowels starts with an uppercase letter, this letter is replaced by its lowercase version and Ab is inserted before the sequence of vowels. 
As vowels, we consider the letters a, e, i, o and u (both their lowercase and uppercase versions). You are asked to:

- Write a function isVowel that takes a single character as its argument.
The function must return a Boolean value that indicates whether or not the given character is a vowel.

- Write a function encode that takes a word or sentence as its string argument. 
The function must return the given word or sentence, translated into Turkey Irish.

- Write a function decode that takes a Turkey Irish word or sentence as its string argument.
The function must return the original word or sentence.
'''


def isVowel(alpha):
    vowel = "aeiou"
    alpha = alpha.lower()
    if alpha in vowel:
        return True
    else:
        return False


def encode(alpha):
    new_string = ""
    consecutive_string = ""
    vowel = "aeiou"
    vowel2 = "AEIOU"
    ctr = 0
    ctr1 = 0
    for i in alpha:
        if i in vowel:
            ctr += 1
            consecutive_string += i
        if i in vowel2:
            ctr1 += 1
            consecutive_string += i
        if i not in vowel and i not in vowel2:
            if ctr >= 1 and ctr1 >= 1:
                new_string += "Ab"
                consecutive_string = consecutive_string[0].lower() + consecutive_string[1:]
                new_string += consecutive_string
                ctr1 = 0
                ctr = 0
                consecutive_string = ""
            if ctr >= 1:
                new_string += "ab"
                new_string += consecutive_string
                ctr = 0
                consecutive_string = ""
            if ctr1 >= 1:
                new_string += "Ab"
                consecutive_string = consecutive_string[0].lower() + consecutive_string[1:]
                new_string += consecutive_string
                ctr1 = 0
                consecutive_string = ""
            new_string += i
    if ctr + ctr1 == len(alpha):
        if alpha[0] in vowel2:
            new_string += "Ab"
            new_string += alpha[0].lower() + alpha[1:]
            ctr = 0
            ctr1 = 0
    if ctr >= 1:
        new_string += "ab"
        new_string += alpha[-ctr:]
    if ctr1 >= 1:
        new_string += 'Ab'
        new_string += alpha[-ctr1].lower()
    return new_string

def decode(alpha):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel2 = ['A', 'E', 'I', 'O', 'U']
    new_list = []
    i = 0
    while i < len(alpha):
        if alpha[i].lower() not in vowel:
            new_list.append(alpha[i])
            i += 1
        if alpha[i:i+2].lower() == 'ab':
            if alpha[i:i+2] == 'Ab':
                new_list.append(alpha[i+2].upper())
            else:
                new_list.append(alpha[i + 2])
            i += 3
            while  i < len(alpha) and alpha[i] in vowel:
                new_list.append(alpha[i])
                i += 1
            while i < len(alpha) and alpha[i] in vowel2:
                new_list.append(alpha[i])
                i += 1
    return ''.join(new_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
'''
>>> isVowel('a')
True
>>> isVowel('c')
False
>>> isVowel('E')
True

>>> encode('Fabiano')
'Fabababianabo'
>>> encode('CIA-agent')
'CAbiA-abagabent'

>>> decode('Fabababianabo')
'Fabiano'
>>> decode('CAbiA-abagabent')
'CIA-agent'
'''
