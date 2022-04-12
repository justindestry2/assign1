#author: justin destry hall
#date: april 08 2022
#descirption: code for assignment 1, csci 141
print("Welcome to the Money Translator!")

#from os import sep

import sys 
#sys.argv for testings for 3 input values  

usernetworth = float(input("What is your yearly income? "))
#usernetworth = float(sys.argv[1])
#adjust user net worth with federal poverty level 2022 -13,590$
costofliving = 13590
usernetworth = float(usernetworth-costofliving)
#name of person making the donation
#capitalize for further use in code
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
print("If ", donatorname, "'s networth is $", actualnetworth,end=",")

#reformating actualnetworth back to int after reformating to str
actualnetworth = actualnetworth.replace(",","")
actualnetworth = float(actualnetworth)

#percentage of donation to net worth would be donation amount divided by acutal net worth
donationdivide = donationamt / actualnetworth
#user donation comparison would be donationdivde(the percentage of networth actually donated)
#multiplied by the users net worth
userdonation = usernetworth * donationdivide
userdonation = "{0:,.4f}".format(userdonation)
usernetworth = usernetworth+costofliving
#reformated usernetworth cause it was only showing 1 penny
usernetworth = "{0:,.2f}".format(usernetworth)
donationamt= "{0:,.2f}".format(donationamt)

#added back costofliving into actualnetworth for final string
#usernetworth = usernetworth+costofliving
#changed one last time for formating in final string
actualnetworth= "{0:,.2f}".format(actualnetworth)
costofliving = "{0:,.2f}".format(costofliving)


#print comparison
print("then one ${} donation for someone with their net worth of ${} is the same as a ${} donation for someone with a net worth of ${} minus the cost of living(${}). Generous?".format(donationamt, actualnetworth, userdonation, usernetworth,costofliving))



