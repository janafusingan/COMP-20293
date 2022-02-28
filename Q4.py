import random

monthDict = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December",
}

num = [x for x in range(1, 13)]     # range(start, stop), will print 1 to 12

ans = True
while(ans is True):
    print()
    print("Available Numbers :", num)
    print()

    rand_num = random.choice(num)
    print("Picked Number is ", rand_num)
    print()

    num.remove(rand_num)
    for key, val in monthDict.items():
        if rand_num is key:
            print("Month Name is", val)
            print()

    a = input("Do you want to pick another number [Y/N] ? ")  # ans will stay True if 'a' is Y / y
    print()
    if a == 'N' or a == 'n' or not num:
        # if num, this is true when num have values and false when empty. hence if not num to reverse it
        print("Thank you for using this program")
        print()
        ans = False
