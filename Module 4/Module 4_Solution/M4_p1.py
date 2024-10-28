

# Program to calculate the tip amount for a restaurant bill.
# User enters bill amount and percentage tip, and program calculates
# tip amount.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

def main():
   bill = bill_to_float(input("How much was your bill? "))
   percent = percent_to_float(input("How much do you want to tip? "))
   tip = bill * percent
   print(f"You should leave a ${tip:.2f} tip")

def bill_to_float(b):
  return round(float(b[1:]),2)
  

def percent_to_float(p):
  return float(p[:len(p)-1])/100.0

try:
  main()
except:
  print("Something is not right!")