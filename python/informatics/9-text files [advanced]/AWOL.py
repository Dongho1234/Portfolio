'''
- Write a function coordinates that takes the location of a CSV file as an argument.
This file must contain information about a number of airports, in the format as described in the introduction of this assignment.
The function must return a dictionary that maps the unique 3-letter code of each airport in the file onto the coordinates of the airport.

- Write a function haversine that takes the coordinates of two locations as its arguments. 
The function must return the Haversine distance between the two locations, under the assumption that Earth is a sphere with radius r = 6371km.
Note that the trigonometric functions (sin, cos, ...) in the math module expect that angles are expressed in radians, not in degrees.
However, the math module also has two functions degrees and radians that can be used to convert angles from radians to degrees, and vice versa.

- Use the function haversine to write a function flightplan that can be used to determine the route of an airplane. 
Three arguments must be passed to the function. The first two arguments represent the unique 3-letter code of the airports of departure and arrival. 
The third argument is a dictionary mapping the unique 3-letter codes of airports onto their coordinates.
In addition, the function has an extra optional parameter range that can be used to pass the range of the airplane (expressed in kilometers; default value:1000km).
The function must return the list of 3-letter codes of all airports the airplane will visit on its route from the airport of arrival to the airport of destination, 
in case the route planning algorithm given above is used. This means that the first and last airports in the list respectively are the airports of departure and arrival.
In case the flight planning algorithm ends up in a situation where no more airports can be reached that meet the required conditions,
the function must raise an AssertionError with the message no possible route.
'''


'''
Student name: Dong ho Lee
Student number: 01614385
'''

import math
import csv
def coordinates(word):
    with open('airports.csv', newline ='', encoding='utf-8') as csvfile:
        reader1 = csv.reader(csvfile)
        dict = {}
        for line in reader1:
            dict[line[0]] = (float(line[5])), (float(line[6])) #make dictionary with key and value
        return dict
def haversine(cord1, cord2):
    b1 = math.radians(cord1[0])
    l1 = math.radians(cord1[1])
    b2 = math.radians(cord2[0])
    l2 = math.radians(cord2[1])
    # convert from degrees to radians
    first_part = (math.sin((b2-b1)/2))**2
    second_part = math.cos(b1)*math.cos(b2)*(math.sin((l2-l1)/2))**2
    a = first_part + second_part
    c = math.atan((a/(1-a))**(1/2))
    r = 6371
    d = 2*r*c
    return d
def flightplan(letter, letter2, coords, range=1000):
    arrival = coords[letter2]
    stopover = [] # for stopover candidates
    list1 = [letter] #for actual stopover
    distance_list = [] # list for camparing distance containing stopovers
    coord_list = [] #list for coordinates to find minimum value
    while list1[-1] != letter2:
        for city in coords:
            distance = haversine(coords[list1[-1]], coords[city])
            if distance <= range:
                stopover.append(city)
        for i in stopover: #i = candidates
            distance_list.append(haversine(coords[i], arrival))
            coord_list.append(haversine(coords[i], arrival))
            distance_list.append(i)
        minimum = min(coord_list)
        position = distance_list.index(minimum) #find index in distance_list
        next_stopover = distance_list[position+1] #coord after is where next_stopover is
        list1.append(next_stopover)
        if list1[-1] != letter2 and minimum > range and range < 1000:
            # riase assertion error following condition b/c range
            raise AssertionError ('no possible route')
        #initialize it
        stopover = []
        distance_list = []
        coord_list = []
    return list1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
'''
>>> coords = coordinates('airports.csv')
>>> len(coords)
9187
>>> type(coords)
<class 'dict'>
>>> coords['BRU']
(50.902222, 4.485833)
>>> coords['CDG']
(49.016667, 2.55)
>>> coords['DCA']
(38.851944, -77.037778)
>>> coords['LAX']
(33.9425, -118.407222)

>>> haversine((50.902222, 4.485833), (49.016667, 2.55)) # BRU <-> CDG
251.2480027355068
>>> haversine((38.851944, -77.037778), (33.9425, -118.407222)) # DCA <-> LAX
3710.8262543589817

>>> flightplan('DCA', 'LAX', coords)
['DCA', 'MTO', 'HLC', 'BFG', 'LAX']
>>> flightplan('DCA', 'LAX', coords, range=2000)
['DCA', 'DDC', 'LAX']
>>> flightplan('DCA', 'LAX', coords, range=4000)
['DCA', 'LAX']

>>> flightplan('BRU', 'CDG', coords)
['BRU', 'CDG']
>>> flightplan('BRU', 'CDG', coords, range=50)
Traceback (most recent call last):
AssertionError: no possible route
'''
