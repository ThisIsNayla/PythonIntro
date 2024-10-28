# Program that adds student records containing student's name, three exam grades, 
# average numeric grade, and average letter grade to a CSV file.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

file = open("grades.csv","a")

while(True):

   lastName = input("\nEnter student's last name: ").title()
   if lastName == "":
      break
   else:
      firstName = input("Enter student's first name: ").title()
      exam1 = input("Enter exam 1 grade: ")
      exam2 = input("Enter exam 2 grade: ")
      exam3 = input("Enter exam 3 grade: ")
      try:
         average = int((int(exam1) + int(exam2) + int(exam3))/3.0)
         if average >= 90:
            letter = "A"
         elif average >= 80:
            letter = "B"
         elif average >= 70:
            letter = "C"
         elif average >= 60:
            letter = "D"
         else:
            letter = "F"
            
         file.write(lastName+","+firstName+","+exam1+","+exam2+","+exam3+","+str(average)+","+letter+"\n")
      except:
         print("Invalid input.")
      
file.close()