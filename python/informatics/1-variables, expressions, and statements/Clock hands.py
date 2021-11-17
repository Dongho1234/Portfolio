'''
INPUT
Two lines containing a single integer. 
These numbers respectively represent the hours h ∈ N (0 <= h <= 23) and minutes m ∈ N (0 <= m <= 59) of the current time in 24-hour notation.

'''
'''
OUTPUT
The sentence:
At uu:mm both hands form an angle of gg°.

where the italic fragments need to filled up with values derived from the input values. 
The placeholders uu and mm need to be filled up respectively with the given hours and minutes of the current time in 24-hour notation.
Both numbers need to be formatted using two digits, with an extra leading zero if needed.
The placeholder gg needs to be filled up with the smallest angle (expressed in degrees) that is formed by the two hands of a 12-hour clock at the given time.
This angle needs to be formatted as a floating point number with a single decimal digit.
Rounding must be used to determine the decimal digits.
'''


y = int(input())
z = int(input())

short = y*30 + z*0.5
long = z*6


c = float(abs(long-short))

T = str(y).zfill(2) + ":" + str(z).zfill(2)
if c >= 360:
    c = (720 - c)
if c >= 180:
    c = abs(360 - c)
    
print("At", T, "both hands form an angle of", str(c)+"°.")


'''
16
37
stdout
At 16:37 both hands form an angle of 83.5°.
'''

