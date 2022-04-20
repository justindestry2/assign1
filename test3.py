#author: justin destry hall
#date: april 07 2022
#description: code for assignment 1, csci 141

#import sys for sys.argvs argument usage in terminal
from builtins import print
import sys 

#welcome message w/ or w/o sys.argvs
print("Welcome to the Modulo-o-matic")

#if using arguments in terminal
if len(sys.argv) > 1:
    #print statements inputing sys.argvs
    print("What is the first number? ", sys.argv[1])
    print("What is the second number? ", sys.argv[2])
    print("What do you think", sys.argv[1], "modulo", sys.argv[2], "is?:", sys.argv[3])
    print("What do you think", sys.argv[2], "modulo", sys.argv[1], "is?:", sys.argv[4])
    #modulos formulas
    #flip back to int before modulo calculations
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    moduloanswer = num1 % num2
    moduloanswer2 = num2 % num1
    moduloguess = sys.argv[3]
    moduloguess2 = sys.argv[4]
    print("You answered", sys.argv[3], "the correct answer is", moduloanswer)
    print("You answered", sys.argv[4], "the correct answer is", moduloanswer2)
    print("Keep up the good work learning!")

#else: only running program with no arguments 
else:
    #input statements for running code as normal
    #prompts user for 2 numbers and 2 modulos calculations
    num1 = (input("What is the first number?"))
    num2 = (input("What is the second number?"))
    moduloguess = (input("What do you think " + num1 + " modulo " + num2 + " is?"))
    moduloguess2 = (input("What do you think " + num2 + " modulo " + num1 + " is?"))
    #modulo formulas
    #flip back to int before modulo calculations
    num1 = int(num1)
    num2 = int(num2)
    moduloanswer = num1 % num2
    moduloanswer2 = num2 % num1
    #turn num1 & num2 back to string to format for print statement 
    num1 = str(num1)
    num2 = str(num2)     
    print("You answered {} the correct answer is {}".format(moduloguess, moduloanswer))
    print("You answered {}, the correct answer is {}".format(moduloguess2,moduloanswer2))
    print("Keep up the good work learning!!")

