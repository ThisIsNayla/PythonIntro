
# Program that calculates the series: 1 + 1/2 + 1/3 + ... + 1/N
# 
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   N = int(input("Please enter the value of N: "))
   if N <= 0:
      print("Invalid input.")
   else:
      a = 0.0
      for i in range (1,N+1):
         a = a + 1/i
      print(f"The sum of the series is: {a:.3f}")
except:
   print("Invalid input.")