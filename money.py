#author: justin destry hall
#date: april 08 2022
#descirption: code for assignment 1, csci 141
print("Welcome to the Money Translator!")

import sys 

#ask for average persons net worth 
usernetworth = float(input("What is your yearly income? "))
#usernetworth = float(sys.argv[1])

#name of person making the donation
donatorname = input("Who is making such an AMAZING donation?")
donatorname = donatorname.capitalize()

#how much of a donation they are making
donationamt = int(input("How much is {} donating???".format(donatorname)))
#donationamt = float(sys.argv[2])

#what their networth is
donatornetworth = int(input("What is {}'s networth in millions?".format(donatorname)))
#donatornetworth = int(sys.argv[3])

actualnetworth = donatornetworth * 1000000 
#reformating actualnetworth for print
actualnetworth = "{0:,.2f}".format(actualnetworth)

#print donators worth in actual amount
print("If ", donatorname, "'s networth is $", actualnetworth)

#reformating actualnetworth back to int after reformating to str
actualnetworth = actualnetworth.replace(",","")
actualnetworth = float(actualnetworth)

#divide donation by networth
donationdivide = donationamt / actualnetworth
#donationdivide = (donationdivide)
#print(donationdivide)
#print comparison
userdonation = usernetworth * donationdivide
userdonation = "{0:,.4f}".format(userdonation)
#reformated usernetworth cause it was only showing 1 penny
usernetworth = "{0:,.2f}".format(usernetworth)
donationamt= "{0:,.2f}".format(donationamt)
#changed one last time for formating in final string
actualnetworth = "{0:,.2f}".format(actualnetworth)

print("Then one ${} donation for someone with their net worth of ${}, is the same as a ${} donation for someone with a net worth of ${} Generous?".format(donationamt, actualnetworth, userdonation, usernetworth))



