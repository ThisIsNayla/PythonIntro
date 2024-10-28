
# Program that uses a function calcGrade to convert a score between 0.0 and 1.0 
# to a letter grade based on the following conversion table:
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

def calcGrade(score):
   if score < 0.0 or score > 1.0:
      grade = "Bad score"
   elif score >= 0.9:
      grade = "A"
   elif score >= 0.8:
      grade = "B"
   elif score >= 0.7:
      grade = "C"
   elif score >= 0.6:
      grade = "D"
   else:
      grade = "F"

   return (grade)


try:
   inscore = float(input("Please enter score: "))
   print(f"Grade: {calcGrade(inscore)}")
      
except:
   print("Bad score.")

