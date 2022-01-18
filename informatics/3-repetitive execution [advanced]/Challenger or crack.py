'''
Input
Decide based on the run of the game in a question round of De Canvascrack, whether the challenger or the crack wins the round. 
The first line contains a number n ∈ N0 that indicates the number of questions in the round.
This is followed by another three lines for each question, that contain the following information:

the correct answer to the question: A, B or C
the answer given by the challenger: A, B or C
the assessment of the crack on the answer given by the challenger: correct or wrong

Output
The crack loses if his total score is less than half of the number of questions in the round.
Otherwise the player with the highest total score wins, or the round ends in a tie if both the challenger and the crack score the same amount of points. 
Depending on the evaluation of the run of the game as described by the information in the input, the following output must be generated:

crack wins: crack wins c points against o
challenger wins: challenger wins o points against c
tie: ex aequo: both contestants score o points

The fragments in italic have to be filled up based on the computed total scores:
c is the total score of the crack and o is the total score of his opponent.
'''

n = int(input()) #number_of_questions_in_the_round

ctr = 0  # challenger
ctr1 = 0  # cracker
i = 0

while True:
    answer = input()  # the_correct_answer_to_the_questions a,b,c
    the_challenger = input()  # challenger_answer
    correct_or_wrong = input()  # crack's_answer
    i += 1
    if answer == the_challenger and correct_or_wrong == "correct":
        ctr += 1
        ctr1 += 1
    elif answer == the_challenger and correct_or_wrong == "wrong":
        ctr += 1
    elif answer != the_challenger and correct_or_wrong == "wrong":
        ctr1 += 1
    if i == n:
        break


if ctr1 < float(n/2) or ctr1 < ctr:
    print("challenger wins {} points against {}".format(ctr, ctr1))
elif ctr1 > ctr and ctr1 >= float(n/2):
    print("crack wins {} points against {}".format(ctr1, ctr))
elif ctr1 == ctr:
    print("ex aequo: both contestants score {} points".format(ctr))

    
'''
Example
Input:
5
C
C
correct
B
C
wrong
B
A
correct
A
A
wrong
C
A
wrong

Output:
crack wins 3 points against 2

Example
Input:
5
C
C
correct
A
A
correct
A
A
correct
B
A
correct
A
B
correct

Output:
ex aequo: both contestants score 3 points
