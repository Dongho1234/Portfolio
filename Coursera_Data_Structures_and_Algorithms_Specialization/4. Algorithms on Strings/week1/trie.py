#Uses python3

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

# tree = { node1: { label1: c1, label2: c2, ...}, node2, ... }
# {0: {'A': 1}, 1: {'T': 2}, 2: {'A': 3}}

import sys

def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    index = 1
    for i in range(len(patterns)):
        current = tree[0]
        for letter in patterns[i]:
            if letter in current.keys():
                current = tree[current[letter]]
            else:
                current[letter] = index
                tree[index] = {}
                current = tree[index]
                index = index + 1
    print(tree)
    return tree

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
#    n_patterns = int(input())
#    patterns = [input() for _ in range(n_patterns)]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

