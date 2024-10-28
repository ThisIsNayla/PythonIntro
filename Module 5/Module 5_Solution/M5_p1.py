

# Program asks the user to enter an integer N between 1 and 9 and uses 
# nested loops to display the following pattern:
#
# 1
# 22
# 333
# 4444
# ....
# NNNN......N
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   num = int(input("Please enter an integer between 1 and 9: "))
   if num <= 0 or num > 9:
      print("Invalid input.")
   else:
      for i in range(1,num+1):
         for j in range(i-1):
            print(i,end="")
         print(i)

except:
   print("Invalid input.")