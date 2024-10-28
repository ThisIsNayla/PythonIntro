
# Program to convert a score between 0.0 and 1.0 to a letter grade 
# based on the following conversion table:
# 
# Score	   Grade
# >= 0.9	   A
# >= 0.8	   B
# >= 0.7	   C
# >= 0.6	   D
# < 0.6	   F
# 
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   score = float(input("Please enter score: "))
   
   if score < 0.0 or score > 1.0:
      print("Bad score.")
   elif score >= 0.9:
      print("Grade: A")
   elif score >= 0.8:
      print("Grade: B")
   elif score >= 0.7:
      print("Grade: C")
   elif score >= 0.6:
      print("Grade: D")
   else:
      print("Grade: F")
      
except:
   print("Bad score.")

