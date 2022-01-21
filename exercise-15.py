# 15

hours_work = int(input("Enter hours work in a week  : "))
ot_pay = 0;
reg_pay = 0;
total_pay = 0;

print("")

if hours_work >= 1 and hours_work <= 80:
    if hours_work > 30:
        reg_pay = 250 * 30
        ot_pay = (hours_work - 30) * 350
    else:
        reg_pay = 250 * hours_work
    
    total_pay = ot_pay + reg_pay
    
    print("Your Payroll Details")
    print("Regular Pay          :", reg_pay)
    print("Overtime Pay         :", ot_pay)
    print("Total Weekly Pay     :", total_pay)

else:
    print("Invalid value for working hours. Kindly enter 1 to 80 hours only")