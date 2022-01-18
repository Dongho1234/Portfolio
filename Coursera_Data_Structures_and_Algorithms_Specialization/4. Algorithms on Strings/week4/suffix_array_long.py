# python3
import sys

"""
Build suffix array of the string text and
return a list result of the same length as the text
such that the value result[i] is the index (0-based)
in text where the i-th lexicographically smallest
suffix of text starts.
"""

def sort_characters(text):
    order = [0] *len(text)
    set_char = sorted((set(text)))
    count = [text.count(i) for i in set_char]

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i, c in reversed(list(enumerate(text))):
        count[set_char.index(c)] -= 1
        order[count[set_char.index(c)]] = i
    return order

def char_classes(t, order):
    classes = [0] * len(t)
    for i in range(1, len(t)):
        if t[order[i]] != t[order[i - 1]]:
            classes[order[i]] = classes[order[i - 1]] + 1
        else:
            classes[order[i]] = classes[order[i - 1]]
    return classes

def sort_doubled(text, l, order, clss):
    len_text = len(text)
    count = [0] * len_text
    new_order = [0] * len_text

    for i in range(len_text):
        count[clss[i]] += 1
    for j in range(1, len_text):
        count[j] += count[j - 1]

    for i in range(len_text - 1, -1, -1):
        start = (order[i] - l + len_text) % len_text
        cl = clss[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def update_classes(new_order, clss, l):
    n = len(new_order)
    new_clss = [0] * n
    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = cur + l, (prev + l) % n
        if clss[cur] != clss[prev] or clss[mid] != clss[mid_prev]:
            new_clss[cur] = new_clss[prev] + 1
        else:
            new_clss[cur] = new_clss[prev]
    return new_clss

def build_suffix_array(t):
    order = sort_characters(t)
    classes = char_classes(t, order)
    L = 1
    while L < len(t):
        order = sort_doubled(t, L, order, classes)
        classes = update_classes(order, classes, L)
        L = 2 * L
    return order


if __name__ == '__main__':
    text = input()
    suffix_array = build_suffix_array(text)
    for e in suffix_array:
        print(e, end=' ')
