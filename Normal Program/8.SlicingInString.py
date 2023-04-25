'''Slicing In String:- Used to slice a word or an alphabet from a given string
            SYNTAX==> [starting_position : ending_pos : step]
            NOTE:- Here step cant be ZERO.
                   Value Of starting position not lesser than 0.
                   Value of Ending position can be exeeded. '''

var = "Python"
print(var[0:1:1])       #P
print(var[2:3:1])       #t
print(var[0:1000:1])    #Python

'''REVERSING A STRING USING SLICING'''
X = "Python"
print(X[-1:0:-1])