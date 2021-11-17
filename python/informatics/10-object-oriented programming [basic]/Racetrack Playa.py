'''
Write a class Block that represents blocks having dimensions and a position as described above,
who can move in the two given ways. This class should support at least the following methods:

- An initialization method __init__ having three parameters length, height, width that take integer values (int)
that respectively represent the length, the height and the width of the block. 
The initialization method also has an optional fourth parameter position that 
takes a sequence (list or tuple) containing two integers (int) that indicates the position of the corner point 
at the bottom left of the front face. In case no value is passed explicitly to the position, 
this corner point it located in the origin (0,0) of the base plane.

- A method area (without arguments) that returns the surface area (float) of the block.

- A method volume (without arguments) that returns the volume (float) of the block.

- A method diagonal (without arguments) that returns the length (float) of the space diagonal of the block.

- A method __repr__ (without arguments) that returns a string representation (str) of the current dimensions and position of the block. 
This string must read as a Python expression that creates a new object of the class Block
that has the same dimensions and position as the current dimensions and position of the block on which the method is called. 
The position must always be represented as a tuple containing two integers (int). 
Derive the correct formatting of the string representation from the examples given below.

- A method slide that takes a string argument (str) containing a single letter. 
This letter indicates the direction in which the method should slide the block: 
    to the left (L), to the right (R), forward (F) or backward (B). 
The method must return a reference to the object (Block) on which the method was called, such that method calls can be chained. 
In case no uppercase letter was passed to the method that corresponds to one of the four directions,
the method must raise an AssertionError with the message invalid direction.

- A method tilt that takes a string argument (str) containing a single letter.
This letter indicates the direction in which the method should tilt the block: 
  to the left (L), to the right (R), forward (F) or backward (B). 
The method must return a reference to the object (Block) on which the method was called, such that method calls can be chained. 
In case no uppercase letter was passed to the method that corresponds to one of the four directions, 
the method must raise an AssertionError with the message invalid direction.

- A method sail that takes a string argument (str) with an even length.
The characters of this string must alternate between letters that indicate a type of movement (S for slide and T for tilt) and
letters that indicate a direction (L for left, R for right, F for forward and B for backward).
For example SB means slide backward, TR means tilt to the right, and SBTR means first slide backward and then tilt to the right.
The method must execute the described movements one after the other and return a reference to the object (Block) on which the method was called, 
such that method calls can be chained. 
In case the given string contains a character at an even position that is no uppercase letter representing one of the two types of movement, 
the method must raise an AssertionError with the message invalid movement. 
In case the given string contains a character at an odd position that is no uppercase letter representing one of the four directions, 
the method must raise an AssertionError with the message invalid direction.
'''


import math
class Block():
    def __init__(self, length, height, width, position=(0,0)):
        self.length = length
        self.height = height
        self.width = width
        self.position = tuple(position)
    def area(self):
        return float(2*(self.length * self.width + self.length * self.height + self.height * self.width))
    def volume(self):
        return float(self.length * self.height * self.width)
    def diagonal(self):
        return math.sqrt(self.length**2+self.height**2+self.width**2)
    def __repr__(self):
        return 'Block(length={}, height={}, width={}, position={})'.format(self.length, self.height, self.width, self.position)

    def slide(self, letter):
        a, b = self.position
        if letter == 'R':
            b += self.length
        elif letter == 'L':
            b -= self.length
        elif letter == 'F':
            a += self.width
        elif letter == 'B':
            a -= self.width
        else:
            raise AssertionError('invalid direction')
        self.position = a,b
        return self

    def tilt(self, letter):
        a, b = self.position
        if letter in ('R', 'L'):
            if letter == 'R':
                b += self.length
            else:
                b -= self.height
            self.length, self.height = self.height, self.length
        elif letter in ('F', 'B'):
            if letter == 'F':
                a += self.height
            else:
                a -= self.width
            self.height, self.width = self.width, self.height
        else:
            raise AssertionError('invalid direction')
        self.position = a,b
        return self

    def sail(self, direction):
        for x in direction[::2]:
            if x not in ('S', 'T'):
                raise AssertionError('invalid movement')
        for i in range(0, len(direction)):
            if direction[i] == 'S':
                self.slide(direction[i+1])
            if direction[i] == 'T':
                self.tilt(direction[i+1])
        return self
      
'''
Example
>>> rock = Block(5, 2, 3)
>>> rock
Block(length=5, height=2, width=3, position=(0, 0))
>>> rock.area()
62.0
>>> rock.volume()
30.0
>>> rock.diagonal()
6.164414002968976
>>> rock2 = rock.slide('R')
>>> rock2
Block(length=5, height=2, width=3, position=(0, 5))
>>> rock is rock2
True
>>> rock.slide('F')
Block(length=5, height=2, width=3, position=(3, 5))
>>> rock.tilt('L')
Block(length=2, height=5, width=3, position=(3, 3))
>>> rock.tilt('B')
Block(length=2, height=3, width=5, position=(0, 3))
>>> rock.tilt('B').slide('L').tilt('L').slide('B')
Block(length=5, height=2, width=3, position=(-8, -4))
>>> rock.sail('SB')
Block(length=5, height=2, width=3, position=(-11, -4))
>>> rock.sail('TR')
Block(length=2, height=5, width=3, position=(-11, 1))
>>> rock.sail('SFSFTLSLTBTBSRSFTRTFTRTRSBSF')
Block(length=2, height=3, width=5, position=(-2, 6))

>>> rock.tilt('X')
Traceback (most recent call last):
AssertionError: invalid direction
>>> rock.sail('XY')
Traceback (most recent call last):
AssertionError: invalid movement
>>> rock.sail('TY')
Traceback (most recent call last):
AssertionError: invalid direction
'''






