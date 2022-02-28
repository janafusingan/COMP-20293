g1_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
g2_words = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
g3_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

num = int(input("Enter an integer number [0 to 99] : "))
r = int(num % 10)  # remainder = 0 if 10 % 10    remainder = 8 if 78 % 10
quo = int(num / 10)  # quotient = 1 if 10 / 10

if num >= 0 and num <= 99:
    # prints zero
    if num == 0:
        print("You have entered Zero")                      
    
    # prints one to nine
    elif num > 0 and num < 10:
        print("You have entered", g3_words[r - 1])

    # prints eleven to nineteen
    elif num > 10 and num < 20:
        print("You have entered", g2_words[r - 1])

    # prints 10 and 20 to 99
    else:
        if r > 0:
            print("You have entered", g1_words[quo - 1], g3_words[r - 1])
        else:
            print("You have entered", g1_words[quo - 1])

else:
    print("You have entered Invalid Integer Number")
