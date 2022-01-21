# 12

reg_charge = float(input("Enter Regular Charge : "))
hours = int(input("Enter Rental Hours   : "))
total = 0;

print("Your Rental Bill is")

if hours <= 3:
    total = reg_charge * hours
    print("First three Hours     :", total)
    print("Excess of three hours :", 0)
    print("Total Rental Bill     :", total)

else:
    # init_cost is the charge for the first 3 hours
    init_cost = reg_charge * 3
    # excess_cost is the charge for the excess of 3 hours
    excess_cost = (reg_charge * 0.9) * (hours - 3)
    total = init_cost + excess_cost
    print("First three Hours     :", init_cost)
    print("Excess of three hours :",excess_cost)
    print("Total Rental Bill     :", total)