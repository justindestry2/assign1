#author: justin destry hall
#date: april 07 2022
#description: code for assignment 1, csci 141
print("Welcome to the Modulo-o-matic")

import sys 

#all 4 int-variables copy-pasted with their own test[argv[]] version run through terminal  

#firstnumber = int(sys.argv[1])  
firstnumber = (input("What is the first number?"))
#secondnumber = int(sys.argv[2])
secondnumber = (input("What is the second number?"))
#couldnt format, had to concatenate str + int, switched int to str
#print(type(firstnumber))
#print(type(secondnumber))
firstnumber = str(firstnumber)
secondnumber = str(secondnumber)
#print(type(firstnumber))
#print(type(secondnumber))
#moduloguess = int(sys.argv[3])

#couldnt format these strings, kept giving errors
#moduloguess = int(input("What do you think {} modulo {} is?".format(firstnumber,secondnumber))
moduloguess = (input("What do you think " + firstnumber + " modulo " + secondnumber + " is?"))

#couldnt format these strings, kept giving errors
moduloguess2 = (input("What do you think " + secondnumber + " modulo " + firstnumber + " is?"))
#moduleguess2 = int(input("WHat do you think {} modulo {} is?".format(secondnumber,firstnumber))
#moduleguess2 = int(sys.argv[4])

#flip back to int before modulo calculations
firstnumber = int(firstnumber)
secondnumber = int(secondnumber)

#modulo formulas
moduloanswer = firstnumber % secondnumber
moduloanswer2 = secondnumber % firstnumber


#with system arguments -testing in terminal
#if len(sys.argv) > 0:
    #print("You answered {} the correct answer is {}".format(moduloguess, moduloanswer))
    #print("You answered {}, the correct answer is {}".format(moduleguess2,moduloanswer2))
    #print("Keep up the good work learning!!")


#same print statements as above
print("You answered {}, the correct answer is {}".format(moduloguess, moduloanswer))
print("You answered {}, the correct answer is {}".format(moduloguess2,moduloanswer2))
print("Keep up the good work learning!!")

