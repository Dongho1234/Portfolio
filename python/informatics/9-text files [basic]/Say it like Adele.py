'''
Assignment
Write a function mix that takes two locations of text files as its arguments.
The function may assume that both text files exist. 
The function must repetitively read the next line from each of these files,
and output them one after the other: first the line that was read from the file passed as the first argument,
and then the line that was read from the file passed as the second argument.
This procedure stops as soon as all lines of at least one of the files have been processed. 
All lines from the second file must be enclosed between --> and <--. For example,

if we consider this 12 line text fragment from the song "Martha" of Tom Waits:

          Operator, number, please
          It's been so many years
          Will she remember my old voice
          While I fight the tears?
          Hello, hello there, is this Martha?
          This is old Tom Frost
          And I am calling long distance
          Don't worry 'bout the cost
          'Cause it's been forty years or more
          Now Martha please recall
          Meet me out for coffee
          Where we'll talk about it all
          
        
and mix it with this 4 line text fragment from the song "Hello" of Adele:

          Hello from the other side
          I must have called a thousand times
          To tell you I'm sorry for everything that I've done
          But when I call you never seem to be home

then we get the following 8 lines as a result:

          Operator, number, please
          -->Hello from the other side<--
          It's been so many years
          -->I must have called a thousand times<--
          Will she remember my old voice
          -->To tell you I'm sorry for everything that I've done<--
          While I fight the tears?
          -->But when I call you never seem to be home<--
'''

def mix(text1, text2, text3 = None):
    reader1 = open(text1, 'r')
    reader2 = open(text2, 'r')
    if text3 is not None:
        myfile = open(text3, 'w')
        for line1, line2 in zip(reader1, reader2):
            a = line1.rstrip() + '\n'
            b = '-->'+line2.rstrip()+'<--' + '\n'
            myfile.write(a)
            myfile.write(b)
    if text3 is None:
        for line1, line2 in zip(reader1,reader2):
            print(line1.rstrip())
            print('-->'+line2.rstrip()+'<--')
            
'''
>>> mix('tom_waits.txt', 'adele.txt')
Operator, number, please
-->Hello from the other side<--
It's been so many years
-->I must have called a thousand times<--
Will she remember my old voice
-->To tell you I'm sorry for everything that I've done<--
While I fight the tears?
-->But when I call you never seem to be home<--

>>> mix('tom_waits.txt', 'adele.txt', 'mix.txt')
>>> print(open('mix.txt', 'r').read(), end='')
Operator, number, please
-->Hello from the other side<--
It's been so many years
-->I must have called a thousand times<--
Will she remember my old voice
-->To tell you I'm sorry for everything that I've done<--
While I fight the tears?
-->But when I call you never seem to be home<--
'''

