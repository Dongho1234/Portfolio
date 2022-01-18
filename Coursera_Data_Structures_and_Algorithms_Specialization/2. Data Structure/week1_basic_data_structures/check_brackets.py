# python3

from collections import namedtuple
Bracket = namedtuple("Bracket", ["char", "position"])

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)
        if next in ")]}":
            #if it is empty
            if not opening_brackets_stack:
                return i + 1
            remove = opening_brackets_stack.pop()
            if (remove.char == '(' and next != ')') or (remove.char =='[' and next != ']') or (remove.char == '{' and next != '}'):
                return i + 1
    #if it is not empty
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
