'''
Assignment
Your task is to change gender of the words in a given sentence, where words are defined as the longest sequence of consecutive letters. 
To do this, you proceed as follows:

- Write a function translate that takes two arguments: 
a word and a dictionary that maps words onto words. In case the given word does not occur in the given dictionary, 
the given word should be returned unmodified. In case the given word does occur in the given dictionary, 
the function must return the word onto which the given word is mapped by the dictionary. 
If the given word contains uppercase letters only, so should the word returned by the function.
If the given word starts with an uppercase letter followed by lowercase letters only, so should the word returned by the function.
In all other cases, the word returned by the function should contain lowercase letters only.

- Write a function sexChange that takes two arguments: 
a sentence and a dictionary that maps words onto words. 
The function must return the given sentence, where each word that occurs in the given dictionary is translated as defined by the function translate, 
based on the given dictionary.

- Write a function undoSexChange that takes two arguments:
a sentence and a dictionary that maps words onto words. 
We assume that the given sentence was translated as defined by the function sexChange, based on the given dictionary. 
The function undoSexChange must undo this translation, and return the original sentence.
'''


def translate(word, translations):
    dict = translations
    if word.islower():
        if word not in dict:
            return word
        else:
            return dict[word]
    if word.isupper():
        word = word.lower()
        if word not in dict:
            return word.upper()
        else:
            return dict[word].upper()
    if word[0].isupper():
        word = word.lower()
        if word not in dict:
            return word.capitalize()
        else:
            a = dict[word]
            return a.capitalize()
    else:
        return word

def sexChange(sentence, translations):
    list = []
    sentence = sentence.split(' ')
    for i in sentence:
        if i.isalpha():
            each = translate(i, translations)
            list.append(each)
        if not i.isalpha():
            if i[:-1].isalpha():
                list.append(translate(i[:-1], translations)+translate(i[-1], translations))
            elif '-' in i:
                i = i.split('-')
                list.append(translate(i[0], translations)+'-'+translate(i[1], translations))
            elif i[0] == "'":
                list.append("'"+translate(i[1:-1], translations)+"'")
            else:
                letter = translate(i[:-2], translations)
                word = letter + i[-2] +i[-1]
                list.append(word)
    return ' '.join(list)

def  undoSexChange(sentence, translations):
    newdict = {}
    key = []
    value = []
    for item in translations:
        value.append(item)
        key.append(translations[item])
    count = 0
    for i in key:
        newdict.update({i: value[count]})
        count += 1
    a = sexChange(sentence, newdict)
    return a

if __name__ == '__main__':
    import doctest
    doctest.testmod()

'''
>>> translations = {'he':'she', 'brother':'sister'}
>>> translate('he', translations)
'she'
>>> translate('HE', translations)
'SHE'
>>> translate('He', translations)
'She'
>>> translate('brother', translations)
'sister'
>>> translate('my', translations)
'my'

>>> sexChange('He is my brother.', translations)
'She is my sister.'

>>> undoSexChange('She is my sister.', translations)
'He is my brother.'
'''

