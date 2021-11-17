'''
Assignment
Write a function pattern that takes a string as its argument.
The function must return the string that is obtained by replacing all vowels (a, e, i, o and u and their upper case versions)
in the given string by an underscore (_). This result is called the pattern of the given string.

Write a function bloopers that takes the location of a text file. 
This text file must contains a sequence of sentences, each on a separate line.
The function must return a dictionary whose keys are the patterns of all sentences that occur in the given text file.
Each key must be mapped onto the set of sentences from the text file that have this key as their pattern. 
The function also has two optional parameters length and occurrences, that both have 1 as their default value.
The dictionary returned by the function may only contain key/value pairs whose key contains at least length characters 
and whose value set contains at least occurrences elements.
'''

def pattern(word):
    vowel = 'aeiouAEIOU'
    new_word = ''
    for i in word:
        if i in vowel:
            new_word += '_'
        else:
            new_word += i
    return new_word

def bloopers(text1, occurrences=1, length=1):
    reader1 = open(text1, 'r')
    dict = {}
    dict1 = {}
    for line1 in reader1:
        value = line1.rstrip()
        key = pattern(value)
        if key not in dict:
            dict[key] = {value}
        else:
            dict[key].add(value)
    for k,i in dict.items():
        if len(k) >= length and len(i) >= occurrences:
            if k not in dict1:
                dict1[k] = i
            else:
                dict1[k].add(i)
    return dict1

  
'''
>>> pattern('AC Melon')
'_C M_l_n'
>>> pattern('slipstack')
'sl_pst_ck'
>>> pattern('Wander Women')
'W_nd_r W_m_n'

>>> candidates = bloopers('wheeloffortune.txt')
>>> candidates['_C M_l_n']
{'AC Melon', 'AC Milan'}
>>> candidates['sl_pst_ck']
{'slapstick', 'slipstack'}
>>> candidates['W_nd_r W_m_n']
{'Winder Woman', 'Wander Women', 'Wonder Woman'}

>>> bloopers('wheeloffortune.txt', length=13)
{'B_tm_n _nd R_b_n': {'Batman and Robin', 'Batmen and Reban'}}
>>> bloopers('wheeloffortune.txt', occurrences=3)
{'W_nd_r W_m_n': {'Wander Women', 'Winder Woman', 'Wonder Woman'}}
>>> bloopers('wheeloffortune.txt', occurrences=2, length=12)
{'W_nd_r W_m_n': {'Wander Women', 'Winder Woman', 'Wonder Woman'}, 'B_tm_n _nd R_b_n': {'Batman and Robin', 'Batmen and Reban'}}
'''
