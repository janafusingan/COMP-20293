# 14

hours_work = int(input("Enter hours work in a week  : "))
hourly_rate = float(input("Enter  employee hourly rate : "))
ot_pay = 0;
reg_pay = 40 * hourly_rate;
total_pay = 0;

print("")

if hours_work >= 40 and hours_work <= 100:
    if hours_work > 40:
        ot_pay = (hours_work - 40) * (hourly_rate + (hourly_rate * 0.5))
        
    total_pay = ot_pay + reg_pay
    
    print("Your Payroll Details")
    print("Regular Pay          :", reg_pay)
    print("Overtime Pay         :", ot_pay)
    print("Total Weekly Pay     :", total_pay)

else:
    print("Invalid hours, Valid values : 40 to 100 hours only")