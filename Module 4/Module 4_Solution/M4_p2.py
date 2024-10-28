

# Program that uses a function calcPay to calculate total wages from 
# hourly rate and hour worked while accounting for 1.5 times hourly rate 
# for work beyond 40 hours. Uses try-except to catch non-numeric input.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

def calcPay (hours, rate):
  if (hours > 40):
    overtime = hours - 40
    wages = (40 * rate) + (overtime * rate * 1.5)
  else:
    wages = hours * rate
  return wages

try:
   rate = float(input("Please enter hourly rate: "))
   hours = float(input("Please enter hours worked: "))
     
   print("Wages =", calcPay(hours, rate))
   
except:
   print("Invalid input. Please use numeric values.")