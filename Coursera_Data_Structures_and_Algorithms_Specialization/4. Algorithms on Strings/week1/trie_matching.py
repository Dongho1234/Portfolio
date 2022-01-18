# python3
import sys


def trie_matching(text,trie):
    ctr = 0
    for i in range(len(text)):
        symbol = text[i]
        if trie[ctr].__contains__(symbol):
            ctr = trie[ctr][symbol]
            if not trie.__contains__(ctr) or trie[ctr] == {}:
                return True
        else:
            return False

def solve(text, trie):
    result = []
    for i in range(len(text)):
        check = trie_matching(text[i:], trie)
        if check:
            result.append(i)
    return result

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1
    for pattern in patterns:
        current = tree[0]
        for letter in pattern:
            if letter in current.keys():
                current = tree[current[letter]]
            else:
                current[letter] = index
                tree[index] = {}
                current = tree[index]
                index = index + 1

    return tree

if __name__ == "__main__":
    text = input()
    n_patterns = int(input())
    patterns = list(input() for _ in range(n_patterns))
    tree = build_trie(patterns)
    result = solve(text, tree)
    for pos in result:
        print(pos, end=' ')
