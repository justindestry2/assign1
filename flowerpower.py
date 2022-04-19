#author: justin destry hall
#date: april 17 2022
#description: code for assignment 2, csci 141
import sys
print("Welcome to Flower Power!")



if len(sys.argv) > 1:
    sunflowers = int(sys.argv[1])
    plumerias = int(sys.argv[2])
    sftrade = int(sys.argv[3])
    pltrade = int(sys.argv[4])

    if sftrade > sunflowers or pltrade > plumerias: 
        print("The perfumer got angry with your lies and ran off!")
    elif sftrade == 0 and pltrade == 0:
        print("The perfumer was disappointed in you and took off.")
    elif sftrade < 11 and pltrade < 6:
        emeraldoffer = sftrade * 2
        print("The perfumer offers you", emeraldoffer, "emeralds")
        #tradeanswer = input("Do you accept the trade? Y/N:")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You trade with the perfumer and walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            sunflowers = sunflowers + sftrade
            plumerias = plumerias + pltrade
            print("You dont trade with the perfumer and you walk away with", sftrade, "sunflowers and", pltrade, "plumeria flowers.")
    elif sftrade < 11 and pltrade >= 6:
        emeraldoffer = pltrade * 3
        print("The perfumer offers you", emeraldoffer, "emeralds")
        #tradeanswer = input("Do you accept the trade? Y/N:")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You trade with the perfumer and walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            sunflowers = sunflowers + sftrade
            plumerias = plumerias + pltrade
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers.")
    elif sftrade % 12 == 0 and not sftrade % 24 == 0 and pltrade < 20:
        emeraldoffer = pltrade
        print("The perfumer offers you", emeraldoffer, "emeralds")
        #tradeanswer = input("Do you accept the trade? Y/N:")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You trade with the perfumer and walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            sunflowers = sunflowers + sftrade
            plumerias = plumerias + pltrade
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers.")
    elif sftrade % 12 == 0 and not sftrade % 24 == 0 and pltrade >= 20:
        emeraldoffer = pltrade * 4
        print("The perfumer offers you", emeraldoffer, "emeralds")
        #tradeanswer = input("Do you accept the trade? Y/N:")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You trade with the perfumer and walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            sunflowers = sunflowers + sftrade
            plumerias = plumerias + pltrade
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers.")
    elif sftrade > 13 and not sftrade % 12 == 0 and sftrade % 24 == 0 and pltrade < 0:
        emeraldoffer = sftrade * 5
        print("The perfumer offers you", emeraldoffer, "emeralds")
       #tradeanswer = input("Do you accept the trade? Y/N:")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You trade with the perfumer and walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            sunflowers = sunflowers + sftrade
            plumerias = plumerias + pltrade
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers.")
    else:
        print("Error!")

    
else:
    sunflowers = int(input("How many sunflowers did you pick up?"))
    plumerias = int(input("How many plumeria flowers did you pick up?"))
    print("As you meander through the forest, you round a corner and a perfumer appears out of nowhere!")
    print("'Watch where you're going', she says. She peers into your bag and her deameanor changes immediately.")
    print("'I have emeralds I can give you for those flowers....")
    sftrade = int(input("How many sunflowers are you willing to trade?"))
    pltrade = int(input("How many plumeria flowers are you willing to trade?"))

    if sftrade > sunflowers or pltrade > plumerias: 
        print("The perfumer got angry with your lies and ran off!")
    elif sftrade == 0 and pltrade == 0:
        print("The perfumer was disappointed in you and took off.")
    elif sftrade < 11 and pltrade < 6:
        emeraldoffer = sftrade * 2
        print("The perfumer offers you", emeraldoffer, "emeralds")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers and 0 emeralds.")
    elif sftrade < 11 and pltrade >= 6:
        emeraldoffer = pltrade * 3
        print("The perfumer offers you", emeraldoffer, "emeralds")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers and 0 emeralds.")
    elif sftrade % 12 == 0 and not sftrade % 24 == 0 and pltrade < 20:
        emeraldoffer = pltrade
        print("The perfumer offers you", emeraldoffer, "emeralds")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers and 0 emeralds.")
    elif sftrade % 12 == 0 and not sftrade % 24 == 0 and pltrade >= 20:
        emeraldoffer = pltrade * 4
        print("The perfumer offers you", emeraldoffer, "emeralds")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers and 0 emeralds.")
    elif sftrade > 13 and not sftrade % 12 == 0 and sftrade % 24 == 0 and pltrade < 0:
        emeraldoffer = sftrade * 5
        print("The perfumer offers you", emeraldoffer, "emeralds")
        tradeanswer = True if input("Do you accept the trade? Y/N:").lower() in ('y', 'yes') else False
        if tradeanswer == True:
            sunflowers = sunflowers - sftrade
            plumerias = plumerias - pltrade
            print("You walk away with", emeraldoffer, "emeralds and", sunflowers, "sunflowers and", plumerias, "plumeria flowers!")
        else:
            print("You dont trade with the perfumer and you walk away with", sunflowers, "sunflowers and", plumerias, "plumeria flowers and 0 emeralds.")
    else:
        print("Error!")
