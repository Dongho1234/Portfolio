
def majority_element(seq, l, r):
    #l = 0, r=len(total_length)
    if l+1 == r:
        return seq[l]
    elif l+2 == r:
        return seq[l]
    m = (l+r)//2
    left = majority_element(seq, l, m)
    right = majority_element(seq, m, r)

    c1, c2 = 0, 0

    for i in seq[l:r]:
        if i == left:
            c1+= 1
        elif i == right:
            c2+= 1
    if c1 > (r-l)//2 and left != -1:
        return left
    elif c2 > (r-l)//2 and right != -1:
        return right
    else:
        return -1

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(int(majority_element(input_elements, 0, input_n) != -1))
