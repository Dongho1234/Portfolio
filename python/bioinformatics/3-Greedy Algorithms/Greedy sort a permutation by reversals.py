

class SignedPermutation():
    def __init__(self, *numbers):
        if type(numbers) == tuple and type(numbers[0]) == list:
            self.numbers = numbers[0]
        else:
            self.numbers = list(numbers)

    def __repr__(self):
        numbers = self.numbers
        if type(numbers[0]) != int:
            numbers = numbers[0]
        if type(numbers) != tuple:
            numbers = tuple(numbers)
        return 'SignedPermutation' + str(numbers)

    def __str__(self):
        numbers = self.numbers
        if type(numbers[0]) != int:
            numbers = numbers[0]
        temp = []
        for i in range(len(numbers)):
            temp.append(numbers[i])
        output = str('(')
        for i in range(len(temp)):
            if temp[i] != ',' and temp[i] != '[' and temp[i] != '[' and int(temp[i]) < 0:
                output += str(temp[i]) + str(' ')
            elif temp[i] != ',' and temp[i] != '[' and temp[i] != '[' and int(temp[i]) > 0:
                output += str('+') + str(temp[i]) + str(' ')
        output = output.strip()
        output += ')'
        return output

    def reversal(self,start,end):
        numbers = self.numbers
        temp= []
        temp = list(numbers)
        if type(temp[0]) != int:
            temp = temp[0]
        subtemp = temp[start:end]
        for i in range(len(subtemp) // 2):
            temp[start+i] = temp[start+i] * -1
            temp[end - 1 - i] = temp[end -1 - i] * -1
            temp[start + i], temp[end -1 - i] = temp[end -1 - i], temp[start + i]
        if len(subtemp)%2 == 1 and end - start != 1:
            temp[start + len(subtemp)//2] = temp[start+len(subtemp)//2] * -1
        if end - start == 1:
            temp[start] = temp[start] * -1
        return SignedPermutation(temp)

    def greedy_sort(self):
        numbers = self.numbers
        index = 0
        index2 = 0
        output = []
        for i in range(1,len(numbers)+1):
            for j in range(1,len(numbers)+1):
                if i == abs(numbers[j-1]):
                    if numbers[j-1] > 0:
                        index = numbers.index(numbers[j-1])
                        index2 = i - 1
                    elif numbers[j-1] < 0:
                        index = j - 1
                        index2 = i - 1
                    if index > index2:
                        index += 1
                        self.numbers = self.reversal(index2, index).numbers
                        numbers = self.numbers
                        a = (index2, index)
                        output.append(a)
                        if numbers[i-1] < 0:
                            self.numbers = self.reversal(index2, index2+1).numbers
                            a = (index2, index2 + 1)
                            output.append(a)
                        break
                    elif index == index2:
                        if numbers[i-1] < 0:
                            self.numbers = self.reversal(index2, index2+1).numbers
                            numbers = self.numbers
                            a = (index2, index2 + 1)
                            output.append(a)
                            break
                        else:
                            break
                    elif index < index2:
                        index2 += 1
                        self.numbers = self.reversal(index, index2).numbers
                        numbers = self.numbers
                        c = (index, index2)
                        output.append(c)
                        if self.numbers[i-1] < 0:
                            self.numbers = self.reversal(index, index+1).numbers
                            numbers = self.numbers
                            a = (index, index + 1)
                            output.append(a)
                        break
        return tuple(output)


'''
permutation_01 = SignedPermutation(-3, 4, 1, 5, -2)
permutation_01
return
SignedPermutation(-3, 4, 1, 5, -2)
print(permutation_01)
stdout
(-3 +4 +1 +5 -2)
permutation_01.reversal(0, 3)
return
SignedPermutation(-1, -4, 3, 5, -2)
permutation_01.reversal(2, 4)
return
SignedPermutation(-3, 4, -5, -1, -2)
'''

'''tuple(SignedPermutation(-1, 5, -3, -10, 8, 9, -7, 4, -2, -6).greedy_sort())
return
((0, 1), (1, 9), (2, 8), (2, 3), (3, 8), (3, 4), (4, 9), (5, 10), (7, 9))
tuple(SignedPermutation(14, -10, 12, 8, -20, 18, 5, -11, -4, -1, 15, -19, -17, -16, -21, -7, 9, 3, -13, -2, -6).greedy_sort())
return
((0, 10), (1, 20), (2, 4), (3, 20), (4, 6), (5, 21), (6, 9), (6, 7), (7, 18), (7, 8), (8, 18), (9, 17), (10, 21), (10, 11), 
(11, 14), (12, 15), (12, 13), (13, 21), (13, 14), (15, 18), (17, 21), (17, 18), (18, 21), (19, 21))

'''
