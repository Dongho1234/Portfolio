# python3

'''
Find all the occurrences of the pattern in the text
and return a list of all positions in the text
where the pattern starts in the text.
'''

import sys
def find_pattern(total):
    s = [0] * len(total)
    border = 0
    for i in range(1, len(total)):
        while border > 0 and total[i] != total[border]:
          border = s[border -1]
        if total[i] == total[border]:
          border += 1
        else:
          border = 0
        s[i] = border
    return s

def KMP(pattern, text):
    total = pattern + '$' + text
    ans = find_pattern(total)
    result = []
    for i in range(len(pattern)+1, len(total)):
      if ans[i] == len(pattern):
        result.append(i- 2 * len(pattern))
    return result



if __name__ == '__main__':
    pattern = input()
    text = input()
    positions = KMP(pattern, text)
    for pos in positions:
        print(pos, end=' ')

