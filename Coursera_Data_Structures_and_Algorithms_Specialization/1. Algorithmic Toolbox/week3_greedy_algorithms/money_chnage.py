
def money_change(money):
    assert 0 <= money <= 10 ** 3
    change_money = [10, 5, 1]
    ctr = 0
    i = 0
    while money != 0:
        while money != 0:
            if money >= change_money[i]:
                money -= change_money[i]
                ctr += 1
            if money < change_money[i]:
               i += 1
    return ctr

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
