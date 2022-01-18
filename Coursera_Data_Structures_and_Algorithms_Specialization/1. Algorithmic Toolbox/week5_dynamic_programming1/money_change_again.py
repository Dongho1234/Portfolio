# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(coin):
    coins_given = [1, 3, 4]
    my_list = [0] * (coin+1)
    for i in range(0, len(my_list)):
        if i == 0:
            my_list[i] = 0
        else:
            my_list[i] = len(my_list)
    for index in range(0, len(my_list)):
        if index > 0:
            for i in range(len(coins_given)):
                if coins_given[i] <= index:
                    my_list[index] = min(my_list[index-coins_given[i]] + 1, my_list[index])
    if my_list[-1] == len(my_list):
        return -1
    else:
        return my_list[-1]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
