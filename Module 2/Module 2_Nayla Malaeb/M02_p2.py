# 	Write a program M02_p2.py that asks a user to enter a weight in kilograms (kg) and converts it
# 	to pounds (lbs). Note that there are 2.2 lbs per kg.
# 	Example:
# 	Please enter the weight in kg: 45.6
# 	Weight = 100.32 lbs.

kg = float(input("Please enter the weight in kg: "))
lb = kg * 2.2
print("Weight in pounds =", lb, "lbs.")