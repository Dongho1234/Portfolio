# python3


def compute_min_number_of_refills(distance, max_run, gas_stops):
    #d = total distance
    #m = travel at most
    #n = gas stations
    #  (950, 400, [200, 375, 550, 750])
    #500 200 [100 200 300 400]

    stops = 0
    last_stop = 0
    index = 0
    gas_stops.append(distance)
    while index < len(gas_stops):
        if gas_stops[index] - last_stop <= max_run:
            index += 1
               #500 200 [100 200 300 400] // 500 -400 = 100 -> index append and break
        elif gas_stops[index] - gas_stops[index-1] > max_run or index == 0:
            return -1
        else: # gas_stop[index] - last > max_run == had to refuel last stop
            last_stop = gas_stops[index-1]
            stops += 1
    return stops

if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
