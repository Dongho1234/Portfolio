def minimum_change(coin, coins_given):
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
    if my_list[-1] == len(my_list) :
        return -1
    else:
        return my_list[-1]

'''
>>> minimum_change(100, [25, 10, 5])
4
>>> minimum_change(4, (23, 11, 2, 1))
2
>>> minimum_change(11855, [9, 6, 5])
1318
>>> minimum_change(2, (5, 3))
-1
'''
