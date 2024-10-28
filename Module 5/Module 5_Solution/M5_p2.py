
# Program that adds even or odd numbers between lower and upper bounds.
# 
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   lower = int(input("Enter lower bound: "))
   upper = int(input("Enter upper bound: "))
   even_or_odd = input("Add up even or odd numbers? ").lower()
   
   if lower < 0 or upper < 0 or lower > upper or (even_or_odd != 'e' and even_or_odd != 'o'):
      print("Invalid input.")
   else:
      if even_or_odd == 'e':
         if lower % 2 == 0:
            start = lower
         else:
            start = lower + 1
      else:
         if lower % 2 == 0:
            start = lower + 1
         else:
            start = lower

      sum = 0
      while start <= upper:
         sum = sum + start
         start = start + 2
            
      if even_or_odd == 'e':
         numType = "even"
      else:
         numType = "odd"
         
      print(f"The sum of {numType} numbers between {lower} and {upper} is: {sum}")
      
except:
   print("Invalid input.")