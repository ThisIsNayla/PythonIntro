# 	Write a program M02_p3.py that asks a user to enter their hourly wage and number of hours
#   worked and calculates the user's wages.
# 	Example:
# 	Please enter hourly wage: 5.75
# 	Please enter hours worked: 40
# 	Total wages = 230.0

num_wage = float(input("Please enter hourly wage: "))
num_hours = int(input("Please enter hours worked: "))
total = num_wage * num_hours
print("Total wages =", total)