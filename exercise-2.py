# 2

hr = int(input("Enter number of hours : "))
extra_hr = hr - 3

# if-statements to get the total bill
if(hr > 3):
    total = (3 * 15) + (extra_hr * 10)
else:
    total = hr * 15

print("Total Bill is ", total)