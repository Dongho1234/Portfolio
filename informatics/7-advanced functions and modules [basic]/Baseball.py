'''
- Write a function hit that takes an integer n ∈ N(int,0 <= n <=4). 
The function also has a second optional parameter occupied that may take a sequence (list or tuple) of integers (int), 
representing the bases that were occupied before the batter entered the field. 
The function must return a tuple containing two elements that describe the situation of the game after the batter has stroke an n-base hit: 
i) the points (int) scored by all players of the batting team during that hit and 
ii) all bases that are occupied (list) after the hit.

- Write a function inning that takes a sequence (list or tuple) of integers (int) in the range [0, 4]. 
These integers represent the successive n-base hits of a team during one batting turn. The function must return a tuple containing two elements: 
i) the points (int) scored by the batting team during that batting turn and 
ii) the bases that are occupied (list) at the end of the batting turn.
'''



def hit(number, occupied=[]):
    score = 0
    occupied = list(occupied)
    if occupied == []:
        total_list = [0]
    else:
        total_list = [0] + list(occupied)
    if number == 0:
        return number, occupied
    for i in range(0, len(total_list)):
        total_list[i] += int(number)
    for n in range(0, len(total_list)):
        if total_list[n] >= 4:
            score += 1
    total_list = total_list[:len(total_list)-score]
    return score, list(total_list)

def inning(number):
    occu = []
    score = 0
    for n in number:
        result = hit(n,occu)
        score += result[0]
        occu = result[1]
    return (score, occu)
  
  
'''
Example
>>> hit(2)
(0, [2])
>>> hit(0, [1, 3])
(0, [1, 3])
>>> hit(1, (1, 3))
(1, [1, 2])
>>> hit(2, occupied=[1, 3])
(1, [2, 3])
>>> hit(3, occupied=(1, 3))
(2, [3])
>>> hit(4, occupied=[1, 3])
(3, [])

>>> inning([0, 1, 2, 3, 4])
(4, [])
>>> inning((4, 3, 2, 1, 0))
(2, [1, 3])
>>> inning([1, 1, 2, 1, 0, 0, 1, 3, 0])
(5, [3])
'''
  
