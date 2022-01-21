# 9

dept = str(input("Enter Department Code : "))
dept_code = ['a', 'b', 'c', 'd']

if dept.lower() in dept_code :
    if dept.lower() == dept_code[0]:
        print("Accounting")
    elif dept.lower() == dept_code[1]:
        print("Marketing")
    elif dept.lower() == dept_code[2]:
        print("Sales")
    elif dept.lower() == dept_code[3]:
        print("Purchasing")

else:
    print("Invalid Department Code")
