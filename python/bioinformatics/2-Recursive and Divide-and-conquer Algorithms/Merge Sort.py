def mergesort(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        half = len(my_list) // 2
        left = my_list[:half]
        right = my_list[half:]
        mergesort(left)
        mergesort(right)
        ctr_left = 0
        ctr_right = 0
        ctr_list = 0
        while ctr_left < len(left) and ctr_right < len(right):
            if left[ctr_left] <= right[ctr_right]:
                my_list[ctr_list] = left[ctr_left]
                ctr_left += 1
            else:
                my_list[ctr_list] = right[ctr_right]
                ctr_right += 1
            ctr_list = ctr_list + 1
        while ctr_left < len(left):
            my_list[ctr_list] = left[ctr_left]
            ctr_list += 1
            ctr_left += 1
        while ctr_right < len(right):
            my_list[ctr_list] = right[ctr_right]
            ctr_list += 1
            ctr_right += 1
    return my_list

'''

mergesort([4, 16, 12, 13, 21, 9, 6, 17, 10, 18, 5, 14, 2, 3, 23, 11, 19, 24, 8, 1, 20, 7, 22, 15, 0])
return
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
'''
