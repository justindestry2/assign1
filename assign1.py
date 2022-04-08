#author: justin destry hall
#date: april 08 2022
#description: code for assignment 1, csci 141
print("Welcome to the Modulo-o-matic")

import sys 

firstnumber = int(input("What is the first number?"))
secondnumber = int(input("What is the second number?"))
moduloguess = int(input("What do you think 3 modulo 5 is?"))
moduloanswer = firstnumber % secondnumber
#was thinking of how to put two arguments into a print statement 
#thought about using two different variables
"""
txt = "You answered {},"
txt2 = " the correct answer is {}"
"""
print("You answered {} the correct answer is {}".format(moduloguess, moduloanswer))

moduleguess2 = int(input("WHat do you think 5 modulo 3 is?"))
moduloanswer2 = secondnumber % firstnumber
print("You answered {}, the correct answer is {}".format(moduleguess2,moduloanswer2))
print("Keep up the good work learning!!")

if len(sys.argv) > 0:
    """
    set firstnumber from system argument 1
    set secondnumber from system argument 2
    set moduloguess from system argument 3
    set moduleguess2 from system argument 4 
    """