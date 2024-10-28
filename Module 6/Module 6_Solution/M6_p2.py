# Program that verifies that a password contains at least 8 characters, 
# an uppercase letter, a lowercase letter,a number, and a special character 
# from the set: !"#$%&'()*+,-./:;<=>?@[\]^_`{} 
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

p = input("Enter password: ")

plen = len(p)
upper = 0
lower = 0
nums = 0
special = 0

for i in p:
   if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      upper += 1
   elif i in "abcdefghijklmnopqrstuvwxyz":
      lower += 1
   elif i in "0123456789":
      nums += 1
   elif i in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{}":
      special += 1
      
print("Password length:", plen, end="")
if plen < 8:
   print(" (*)")
else:
   print("")
   
print("Uppercase letters:", upper, end="")
if upper == 0:
   print(" (*)")
else:
   print("")
   
print("Lowercase letters:", lower, end="")
if lower == 0:
   print(" (*)")
else:
   print("")
   
print("Numbers:", nums, end="")
if nums == 0:
   print(" (*)")
else:
   print("")
   
print("Special characters:", special, end="")
if special == 0:
   print(" (*)")
else:
   print("")
   
if plen >= 8 and upper > 0 and lower > 0 and nums > 0 and special > 0:
   print("Status: PASSED")
else:
   print("Status: FAILED")