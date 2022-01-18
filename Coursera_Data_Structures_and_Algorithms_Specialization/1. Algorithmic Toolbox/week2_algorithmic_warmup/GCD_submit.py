def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    while b != 0:

        a, b = b, a % b

    return a



if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
