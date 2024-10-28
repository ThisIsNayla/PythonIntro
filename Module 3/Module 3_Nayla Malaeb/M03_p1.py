# Write a program M03_p1.py that updates the wages program you wrote for your Module 2 assignment (M02_p3.py). In
# addition to asking the user to enter their hourly wage and number of hours worked, your program must calculate the
# total wages using 1.5 times the hourly wage for work done beyond 40 hours.
#
# 	Example:
# 	Please enter hourly wage: 6
# 	Please enter hours worked: 40
# 	Total wages = 240.0
#
# 	Please enter hourly wage: 6
# 	Please enter hours worked: 50
# 	Total wages = 330.0

num_wage = float(input("Please enter hourly wage: "))
num_hours = int(input("Please enter hours worked: "))
total = num_wage * num_hours
if total > 40:
    extra_hours = (1.5 * num_wage) * (num_hours - 40)
    total = (40 * num_wage) + extra_hours
    print("Total wages =", total)
else:
    print("Total wages =", total)