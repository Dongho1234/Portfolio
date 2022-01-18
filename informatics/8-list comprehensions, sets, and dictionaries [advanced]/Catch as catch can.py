'''
Assignment

If n-1 parameter values are known for a linear equation with n ∈ N parameters (with n >= 2), 
the missing parameter value can be computed directly from the formula. 
In this assignment we apply this on the juggling equation.

The parameters of an equation are represented as a container of strings 
(a string, a list, a tuple or a set), where each string contains a valid name for a parameter of a Python function
(the same naming rules apply as for variables: names only contain letters, digits and underscore and do not start with a digit).
All parameter names should also be different.
Your task:

- Write a function missing_parameter that takes two arguments. 
The second argument represents the parameters of an equation. 
The first argument is a dictionary whose keys are all-but-one of the equation parameters.
The function must return a string containing the name of the missing parameter.
In case the keys of the given dictionary are not all-but-one of the given equation parameters,
the function must raise an AssertionError with the message invalid parameters.

- Write a function juggle that takes a dictionary that maps four out of five parameters of the juggling equation onto given values for these parameters.
All given values are strictly positive integers or real numbers. 
The function must return a dictionary that maps all parameters of the juggling equation onto their values:
the means that the given values must be completed with the value of the missing parameter that is computed from the juggling equation. 
All values in this dictionary should be floating point numbers.
In case the keys of the given dictionary are not four out of five parameters of the juggling equation, 
the function must raise an AssertionError with the message invalid parameters.

- Write a function juggler that takes values for four out of five parameters of the juggling equation using named arguments.
The names of the parameters should correspond to the uppercase letters used in the juggling equation,
and all values must be strictly positive integers or real numbers. 
The function must return a dictionary that maps all parameters of the juggling equation onto their values:
the means that the given values must be completed with the value of the missing parameter that is computed from the juggling equation. 
All values in this dictionary should be floating point numbers. 
In case the function is not called with named arguments that correspond to four out of five parameters of the juggling equation,
it must raise an AssertionError with the message invalid parameters.
'''

def missing_parameter(dict, keys):
    keys = list(keys)
    for key in dict:
        if key in keys:
            keys.remove(key)
    keys = '.'.join(keys)
    assert len(keys) == 1, 'invalid parameters'
    return keys

def juggle(dictionary):
    dict = {}
    list = missing_parameter(dictionary, 'FDVBH')
    dict.update(dictionary)
    if 'V' in list:
        values = abs(((dictionary['H']*(dictionary['F']+dictionary['D']))/(dictionary['B'])-dictionary['D']))
        dict.update({'V':float(values)})
    if 'B' in list:
        values = (dictionary['H']*(dictionary['F'] + dictionary['D'])) / (dictionary['V'] + dictionary['D'])
        dict.update({'B':float(values)})
    if 'H' in list:
        values = (dictionary['B']*(dictionary['V'] + dictionary['D'])) / (dictionary['F'] + dictionary['D'])
        dict.update({'H': float(values)})
    if 'F' in list:
        values = abs((dictionary['B']*(dictionary['V'] + dictionary['D'])) / (dictionary['H']) - dictionary['D'])
        dict.update({'F': float(values)})
    if 'D' in list:
        values = (abs((dictionary['B']*dictionary['V']) - (dictionary['H']*(dictionary['F'])))/abs((dictionary['H']-dictionary['B'])))
        dict.update({'D': float(values)})
    for key in dict:
        if isinstance(dict[key], int):
            dict[key] = float('{:.1f}'.format(dict[key]))
    return dict

def juggler(**kwargs):
    return juggle(kwargs)


'''
Example
>>> missing_parameter({'F':1.2, 'D':0.6, 'H':2, 'B':4}, 'FDVBH')
'V'
>>> missing_parameter({'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2}, 'FDVBH')
'F'
>>> missing_parameter({'F':1.2, 'D':0.6, 'H':2, 'X':4}, 'FDVBH')
Traceback (most recent call last):
AssertionError: invalid parameters
>>> missing_parameter({'F':1.2, 'D':0.6, 'H':2}, 'FDVBH')
Traceback (most recent call last):
AssertionError: invalid parameters

>>> juggle({'F':1.2, 'D':0.6, 'H':2, 'B':4})
{'F': 1.2, 'D': 0.6, 'B': 4.0, 'V': 0.3, 'H': 2.0}
>>> juggle({'D': 0.6, 'B': 4, 'V': 0.3, 'H': 2})
{'D': 0.6, 'V': 0.3, 'F': 1.2, 'H': 2.0, 'B': 4.0}
>>> juggle({'F':1.2, 'D':0.6, 'H':2, 'X':4})
Traceback (most recent call last):
AssertionError: invalid parameters

>>> juggler(F=1.2, D=0.6, H=2, B=4)
{'F': 1.2, 'D': 0.6, 'B': 4.0, 'V': 0.3, 'H': 2.0}
>>> juggler(D=0.6, B=4, V=0.3, H=2)
{'D': 0.6, 'V': 0.3, 'F': 1.2, 'H': 2.0, 'B': 4.0}
>>> juggler(F=1.2, D=0.6, H=2, X=4)
Traceback (most recent call last):
AssertionError: invalid parameters
'''
