'''
INPUT
The first line of input contains the name of an animal species. 
This is followed by two more lines of input that each contain a positive integer. 
The first integer is the average number of heartbeats per minute of the species, 
and the second integer is the average life expectancy of the species expressed in years.
'''

'''
Output
The output must contain the sentence creatures have d.dd billion heartbeats,
where the fragments in italic have to filled up with the given and calculated values. 
The placeholder creatures must be filled up with the given name of the animal species. 
The placeholder d.dd must be filled up with the computed number of life time heartbeats of the animal species,
expressed in billions of heartbeats. This value must be expressed as a floating point number with two decimal digits, 
where rounding is used to determine the decimal digits.
The life time heartbeat computation should not need to take into account leap years,
and must consider each year to have 365 days
'''



x = input()
y = int(input())
z = int(input())

second_intger = z*365*24*60
first_intger = y*second_intger*0.000000001

print (x, 'have',"{0:.2f}".format(round(first_intger,2)),'billion heartbeats')

'''
humans
60
70
stdout
humans have 2.21 billion heartbeats
'''
