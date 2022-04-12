#author: justin destry hall
#date: april 07 2022
#description: code for assignment 1, csci 141
import sys 

print("Welcome to the Modulo-o-matic")


if len(sys.argv) > 1:
    print("What is the first number? ", sys.argv[1])
    print("What is the second number? ", sys.argv[2])
    print("What do you think", sys.argv[1], "modulo", sys.argv[2], "is?")
    print("What do you think", sys.argv[2], "modulo", sys.argv[1], "is?")
    firstnumber = int(sys.argv[1])
    secondnumber = int(sys.argv[2])
    moduloanswer = firstnumber % secondnumber
    moduloanswer2 = secondnumber % firstnumber
    print("You answered", sys.argv[3], "the correct answer is", moduloanswer)
    print("You answered", sys.argv[4], "the correct answer is", moduloanswer2)
    print("Keep up the good work learning!")

else:
    firstnumber = (input("What is the first number?"))
    secondnumber = (input("What is the second number?"))
    moduloguess = (input("What do you think " + firstnumber + " modulo " + secondnumber + " is?"))
    moduloguess2 = (input("What do you think " + secondnumber + " modulo " + firstnumber + " is?"))
    #modulo formulas
    #flip back to int before modulo calculations
    firstnumber = int(firstnumber)
    secondnumber = int(secondnumber)
    moduloanswer = firstnumber % secondnumber
    moduloanswer2 = secondnumber % firstnumber
    firstnumber = str(firstnumber)
    secondnumber = str(secondnumber)     
    print("You answered {} the correct answer is {}".format(moduloguess, moduloanswer))
    print("You answered {}, the correct answer is {}".format(moduloguess2,moduloanswer2))
    print("Keep up the good work learning!!")

#firstnumber = (input("What is the first number?"))
#secondnumber = (input("What is the second number?"))
"""
firstnumber = str(firstnumber)
secondnumber = str(secondnumber)

#moduloguess = (input("What do you think " + firstnumber + " modulo " + secondnumber + " is?"))
#moduloguess2 = (input("What do you think " + secondnumber + " modulo " + firstnumber + " is?"))


#flip back to int before modulo calculations
firstnumber = int(firstnumber)
secondnumber = int(secondnumber)

#modulo formulas
moduloanswer = firstnumber % secondnumber
moduloanswer2 = secondnumber % firstnumber



print("You answered {} the correct answer is {}".format(moduloguess, moduloanswer))
print("You answered {}, the correct answer is {}".format(moduloguess2,moduloanswer2))
print("Keep up the good work learning!!")



if len(sys.argv) > 1:
    print("You answered", sys.argv[1], "the correct answer is", sys.argv[2])
    print("You answered", sys.argv[3], "the correct answer is", sys.argv[4])
    print("Keep up the good work learning!")

else len(sys.argv) == 0:
    print("You answered {} the correct answer is {}".format(moduloguess, moduloanswer))
    print("You answered {}, the correct answer is {}".format(moduloguess2,moduloanswer2))
    print("Keep up the good work learning!!")
"""
