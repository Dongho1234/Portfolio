# python3

def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))


#tokens = input()
#num1, num2 = map(int, tokens.strip().split())
#print(num1 + num2)