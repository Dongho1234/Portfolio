
def lcm(a, b):
    save1, save2 = a, b
    while b != 0:

        a, b = b, a % b

    return int(save1*save2 /a)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
