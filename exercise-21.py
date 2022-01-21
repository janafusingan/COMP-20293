# 21

import math

# import math to use the ceil() function 
# ceil() is use to get the largest integer 

dest_code = int(input("Enter DEST. CODE : "))
duration = int(input("Enter Duration   : "))

if dest_code > 0 and dest_code < 5:
    print("TOTAL CHARGES IS P", end=" ")
    if dest_code == 1:
        print(50 * math.ceil(duration/3))
    elif dest_code == 2:
        print(30 * math.ceil(duration/2))
    elif dest_code == 3:
        print(40 * math.ceil(duration/4))
    else:
        print(35 * math.ceil(duration/2))

else:
    print("Invalid Destination Code")