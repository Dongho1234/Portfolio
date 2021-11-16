'''
Write a Python function minimumAverageEndtime that takes a list of execution times for n jobs and returns the minimum average endtime.
'''
def minimumAverageEndtime(my_list):
    for index in range(1, len(my_list)):
        element = my_list[index]
        while index > 0 and my_list[index - 1] > element:
            my_list[index] = my_list[index - 1]
            index = index - 1
            my_list[index] = element
    average_endtime = 0
    total_time = []
    for time in my_list:
        average_endtime = time + average_endtime
        total_time.append(average_endtime)
    return sum(total_time)/len(my_list)

  '''
  >>> minimumAverageEndtime([15, 8, 3, 10])
17.75
'''
