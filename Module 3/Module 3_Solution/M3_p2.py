

# Program to calculate total wages from hourly rate and hour worked while 
# accounting for 1.5 times hourly rate for work beyond 40 hours. 
# Uses try-except to catch non-numeric input.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   rate = float(input("Please enter hourly rate: "))
   hours = float(input("Please enter hours worked: "))

   if (hours > 40):
     overtime = hours - 40
     wages = (40 * rate) + (overtime * rate * 1.5)
   else:
     wages = hours * rate
     
   print("Wages =", wages)
   
except:
   print("Invalid input. Please use numeric values.")