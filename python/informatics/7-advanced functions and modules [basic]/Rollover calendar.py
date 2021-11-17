'''
Assignment
In countries that use the day/month date format, Pi Day should be celebrated on April 31. 
However, the month April only has 30 days. Therefore, we have invented a new calendar 
where it is allowed to continue enumerating the days at the end of the month. 
In this system, April 31 would be just a synonym for May 1.

Your task is to implement a function rollover_date that has three optional parameters: 
day, month and year. These parameters each take an integer (int) that respectively indicates the day, 
the month and the year in our new calendar system, where it is allowed to continue enumerating the days at the end of the month. 
The default values for these parameters are respectively the current day, the current month and the current year. 
The function must return the date (datetime.date) that corresponds to the given date in the regular calendar.

This way, the function call rollover_date(43, 15, 2016) reads as the 43rd day of the 15th month of the year 2016. 
To convert this date to the regular calendar, we first roll over the month to the next year, 
so we end up with March, the third month of the year 2017. 
Now, since March only has 31 days, we roll over the extra days to April, 
so we finally end up with April 12, 2017. Dates that are also valid in the regular calendar, remain unchanged by this procedure. 
Rolling over dates should take leap years into consideration.

'''
from datetime import date
from datetime import timedelta

def rolloverDate(day= None, month= None, year= None):
    today = date.today()
    if year is None:
        year = today.year
    if month is None:
        month = today.month
    if day is None:
        day = today.day
    if month > 12:
        year += (month-1) // 12
        month = (month - 1) % 12 + 1
    hello = date(year, month, 1)
    hello = hello + timedelta(day-1)
    return hello

  if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
    '''
    Example
>>> rollover_date(month=4, day=31)
datetime.date(2016, 5, 1)
>>> rollover_date(year=2016, month=15, day=43)
datetime.date(2017, 4, 12)
>>> rollover_date(year=2016, month=3, day=16)
datetime.date(2016, 3, 16)
>>> rollover_date(year=2016, month=12, day=64)
datetime.date(2017, 2, 2)
>>> rollover_date(year=2016, month=19, day=99)
datetime.date(2017, 10, 7)
>>> rollover_date(year=2016, month=1, day=99999)
datetime.date(2289, 10, 14)
>>> rollover_date(year=2016, month=9999, day=10)
datetime.date(2849, 3, 10)
'''
    
    
