#author: justin destry hall
#date: april 08 2022
#descirption: code for assignment 1, csci 141
print("Welcome to the Money Translator!")

import sys 

#ask for average persons net worth (possibly argv it in)
usernetworth = float(input("What is your income? "))
#usernetworth = float(sys.argv[1])

#name of person making the donation
donatorname = input("Who is making the AMAZING donation?")
donatorname = donatorname.capitalize()

#how much of a donation they are making
donationamt = float(input("How much are they donating???"))
#donationamt = float(sys.argv[2])

#what their networth is
donatornetworth = int(input("What is their networth in millions?"))
#donatornetworth = int(sys.argv[3])

actualnetworth = donatornetworth * 1000000 

#print donators worth in actual amount
print(donatorname, "'s networth is ", actualnetworth)

#divide donation by networth
donationdivide = donationamt // actualnetworth
print(donationdivide)
#print comparison

#compare that percentage to average persons networth

