# 	2. Modify M03_p1.py to use try-except to catch non-numeric input. Save your program as M03_p2.py.
#
# 	Example:
# 	Please enter hourly wage: six
# 	Invalid input. Please use numeric values.
#
# 	Please enter hourly wage: 6
# 	Please enter hours worked: fifty
# 	Invalid input. Please use numeric values.
#
# 	Please enter hourly wage: 6
# 	Please enter hours worked: 50
#   Total wages = 330.0

try:
    num_wage = float(input("Please enter hourly wage: "))
    num_hours = int(input("Please enter hours worked: "))
    total = num_wage * num_hours
    if total > 40:
        extra_hours = (1.5 * num_wage) * (num_hours - 40)
        total = (40 * num_wage) + extra_hours
        print("Total wages =", total)
    else:
        print("Total wages =", total)
except:
    print("Invalid input. Please use numeric values.")