# Bingo Game by Jana Andrea Fusingan from DICT 3-3

import random

print("START OF BINGO GAME")
print("")
print("Available Numbers : ")
print("")
print("B => 01,02,03,04,05,06,07,08,09,10,11,12,13,14,15")
print("I => 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30")
print("N => 31,32,33,34,35,36,37,38,39,40,41,42,43,44,45")
print("G => 46,47,48,49,50,51,52,53,54,55,56,57,58,59,60")
print("O => 61,62,63,64,65,66,67,68,69,70,71,72,73,74,75")
print("")

# initialize allNum to have bingo numbers 1-75
allNum = [[x+1 for x in range(15)], [x+1 for x in range(15, 30)], [x+1 for x in range(30, 45)],
            [x+1 for x in range(45, 60)], [x+1 for x in range(60, 75)]]
# B I N G O list
B_List = []
I_List = []
N_List = []
G_List = []
O_List = []

ans1 = str(input("Do you want to draw a number (Y/N)? "))
g = 1

# will run once
while g == 1:

    if ans1 == 'y' or ans1 == 'Y':
        # draw a num on the allNum list
        # move it to B - O list and
        # remove from allNum

        # generate a random number and check if the num is in the allNum list
        # loops back if the generated number does not exist
        ctr = 0
        while ctr == 0:
            num = random.randrange(1, 75)
            if num in allNum[0] or num in allNum[1] or num in allNum[2] or num in allNum[3] or num in allNum[4]:
                ctr = 1
            else:
                ctr = 0
        # end

        #remove the num in allNum list
        if num <= 15:
            allNum[0].remove(num)
        elif num <= 30:
            allNum[1].remove(num)
        elif num <= 45:
            allNum[2].remove(num)
        elif num <= 60:
            allNum[3].remove(num)
        else:
            allNum[4].remove(num)
        # end remove

        # place the number to the appropriate B-I-N-G-O list and prints it
        print("Random Selected Number :", end="")
        if num <= 15:
            # B
            B_List.append(num)
            print("B -", num)
        elif num <= 30:
            # I
            I_List.append(num)
            print("I -", num)
        elif num <= 45:
            # N
            N_List.append(num)
            print("N -", num)
        elif num <= 60:
            # G
            G_List.append(num)
            print("G -", num)
        else:
            # O
            O_List.append(num)
            print("O -", num)

        input("Press any key to continue...")
        # end

        # print the result
        print("")
        print("Available Number :")
        # print all Available Number
        # start
        ctr = 0     # counter
        for x in allNum:
            # start
            if ctr == 0:
                print("B :", x)
            elif ctr == 1:
                print("I :", x)
            elif ctr == 2:
                print("N :", x)
            elif ctr == 3:
                print("G :", x)
            elif ctr == 4:
                print("O :", x)
            # end
            ctr = ctr + 1
        # end

        print("")
        print("Picked Number :")
        print("B =>", B_List)
        print("I =>", I_List)
        print("N =>", N_List)
        print("G =>", G_List)
        print("O =>", O_List)

        print("")
        if B_List and I_List and N_List and G_List and O_List:
            print("BINGO!!!")
            ans1 = 'n'
        else:
            ans1 = str(input("Do you want to draw a number (Y/N)? "))

    else:
        print("This Bingo Game is over.")
        print()
        ans2 = str(input("Do you want to set another Bingo Game (Y/N)? "))
        print()

        if ans2 == 'y' or ans2 == 'Y':
            # clear / reset all the list
            allNum = [[x+1 for x in range(15)], [x+1 for x in range(15, 30)], [x+1 for x in range(30, 45)],
            [x+1 for x in range(45, 60)], [x+1 for x in range(60, 75)]]
            B_List = []
            I_List = []
            N_List = []
            G_List = []
            O_List = []
            g = 1

            print("START OF BINGO GAME")
            print("")
            print("Available Numbers : ")
            print("")
            print("B => 01,02,03,04,05,06,07,08,09,10,11,12,13,14,15")
            print("I => 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30")
            print("N => 31,32,33,34,35,36,37,38,39,40,41,42,43,44,45")
            print("G => 46,47,48,49,50,51,52,53,54,55,56,57,58,59,60")
            print("O => 61,62,63,64,65,66,67,68,69,70,71,72,73,74,75")
            print("")

            ans1 = str(input("Do you want to draw a number (Y/N)? "))

        # if N / n is the answer, break from the loop
        else:
            print("Thank you for using this Bingo Game program")
            g = 0

