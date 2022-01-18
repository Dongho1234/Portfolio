'''
INPUT
The input is a positive integer that expresses a number of Martian days (sols)
'''

'''
The ouput expresses the given number of sols in Earth solar days, hours, minutes and seconds.
This conversion must equal 1 sol with 24 hours, 39 minutes and 35.244 seconds. 
The exact output format can be derived from the example given below.
All values that occur in the formatted output must be expressed as integers, 
and the number of seconds must be expressed as an integer by simply dropping the decimal digits.
'''



x = int(input())
seconds = x*24*60*60+x*39*60+x*35.244
remaining_second = seconds % 60
minutes = seconds/60
remaining_minutes = minutes % 60
hours = minutes / 60
remaining_hours = hours % 24
days = hours / 24
remaining_days = days
print(x, "sols =", int(remaining_days), "days,", int(remaining_hours), "hours,", int(remaining_minutes), "minutes", "and", int(remaining_second), "seconds")

'''
1377
stdout
1377 sols = 1414 days, 20 hours, 31 minutes and 50 seconds
'''
