# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    my_list = [0, 1]

    if n <= 1:
        return n
    for i in range(2, n+1):
        c = my_list[i-1] + my_list[i-2]
        my_list.append(c)
    return my_list[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
