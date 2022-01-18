class Lemming():
    def __init__(self, text1, position, move):
        self.text1 = open(text1, 'r')
        self.level = [] #read each line
        for line in self.text1.readlines():
            self.level.append(line.strip())
        self.row = 0
        self.col = position #col is where it's input
        self.move = move

    def position(self): #loop unitl next row has #
        while self.level[self.row+1][self.col] != "#":
            self.row += 1
        tup = (self.row, self.col, self.move)
        return tup

    def __str__(self):
        output = ''
        for row in range(len(self.level)):
            # if it is the position while looping, append either < or <,
            # else append as it is,which is the level
            for col in range(len(self.level[row])):
                if row == self.row and col == self.col:
                    output += self.move
                else:
                    output += self.level[row][col]
            output +='\n'
        return output.rstrip()

    def step(self):
        if self.move is '<':
            if self.col == 1: #when face left the wall
                self.move = '>'
            # if it face the wall
            elif self.level[self.row-1][self.col-1] == '#' and self.level[self.row][self.col-1] == '#' and self.col > 1:
                self.move = '>'
            # when face the block, needs to go up
            elif self.level[self.row][self.col-1] == '#' and self.level[self.row-1][self.col-1] != '#':
                self.row -= 1
                self.col -= 1
            #when it's going down
            elif self.level[self.row][self.col-1] != '#' and self.level[self.row+1][self.col-1] != '#':
                while self.level[self.row+1][self.col-1] != '#':
                    self.row += 1
                self.col -= 1
            else:
                self.col -= 1
        elif self.move is '>':
            if self.level[self.row+1][self.col+1] != '#' and self.level[self.row][self.col+1] != '#':
                #if underneath is empty, it has to descending)
                while self.level[self.row+1][self.col+1] != '#':
                    self.row += 1
                self.col += 1
            elif self.level[self.row-1][self.col+1] == '#' and self.level[self.row][self.col+1] == '#':
                #when face the right wall
                self.move = '<'
            elif self.level[self.row][self.col + 1] == '#':
                #when face the block
                self.col += 1
                self.row -= 1
            else:
                self.col += 1
        self.tup = (self.row, self.col, self.move)
        return self.tup

    def steps(self, number):
        list1 = [] #list for all steps
        #loop it 'number' times
        while len(list1) != number:
            a = self.step()
            list1.append(a)
        return list1

'''
>>> lemming = Lemming('level.txt', 3, '<')
>>> lemming.position()
(3, 3, '<')
>>> print(lemming)
#################################
#                               #
#         #                     #
#  <    ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(3, 2, '<')
>>> lemming.step()
(3, 1, '<')
>>> lemming.step()
(3, 1, '>')
>>> lemming.step()
(3, 2, '>')
>>> print(lemming)
#################################
#                               #
#         #                     #
# >     ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.steps(5)
[(3, 3, '>'), (3, 4, '>'), (3, 5, '>'), (3, 6, '>'), (3, 7, '>')]
>>> print(lemming)
#################################
#                               #
#         #                     #
#      >###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(2, 8, '>')
>>> print(lemming)
#################################
#                               #
#       > #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(2, 9, '>')
>>> lemming.step()
(1, 10, '>')
>>> print(lemming)
#################################
#         >                     #
#         #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########  ##############     #
#################################
>>> lemming.step()
(6, 11, '>')
>>> print(lemming)
#################################
#                               #
#         #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########> ##############     #
#################################
>>> lemming.steps(21)
[(6, 12, '>'), (5, 13, '>'), (5, 14, '>'), (4, 15, '>'), (4, 16, '>'), (3, 17, '>'), (3, 18, '>'), (3, 19, '>'), (4, 20, '>'), (4, 21, '>'), (4, 22, '>'), (5, 23, '>'), (5, 24, '>'), (5, 25, '>'), (5, 26, '>'), (6, 27, '>'), (6, 28, '>'), (6, 29, '>'), (6, 30, '>'), (6, 31, '>'), (6, 31, '<')]
>>> lemming.steps(21)
[(6, 30, '<'), (6, 29, '<'), (6, 28, '<'), (6, 27, '<'), (5, 26, '<'), (5, 25, '<'), (5, 24, '<'), (5, 23, '<'), (4, 22, '<'), (4, 21, '<'), (4, 20, '<'), (3, 19, '<'), (3, 18, '<'), (3, 17, '<'), (4, 16, '<'), (4, 15, '<'), (5, 14, '<'), (5, 13, '<'), (6, 12, '<'), (6, 11, '<'), (6, 11, '>')]
>>> print(lemming)
#################################
#                               #
#         #                     #
#       ###                     #
###########      ###            #
###########    ########         #
###########> ##############     #
#################################
'''
