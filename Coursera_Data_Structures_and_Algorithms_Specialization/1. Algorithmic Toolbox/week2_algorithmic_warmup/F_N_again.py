
def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    my_list = [0, 1]
    mod_list = [0, 1]
    if n <= 1:
        return n % m
    ctr = 2
    compare = None
    while True:
        c = my_list[ctr-1] + my_list[ctr-2]
        my_list.append(c)
        mod_list.append(c % m)
        ctr += 1
        if len(mod_list) % 2 == 0:
            half = len(mod_list)//2
            compare1 = mod_list[:half]
            compare2 = mod_list[half:]
            if compare1 == compare2:
                compare = compare1
                break
    #n = x*y + rest
    y = len(compare)
    x = int(n /y)
    #new input = rest
    new_input = n-(x*y)

    #F(newinput) mod m = ans
    return my_list[new_input] % m








if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
