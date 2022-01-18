# python3
import sys

def BWT(text):
    matrix = [text]
    for i in range(1, len(text)):
        text = text[-1] + text[:-1]
        matrix.append(text)
    matrix.sort()
    bwt = ""
    for i in matrix:
        bwt += i[-1]
    return bwt

if __name__ == '__main__':
    text = input()
    print(BWT(text))
