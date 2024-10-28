# Program that prints all letter combinations for a 7-digit phone number.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut


letters = ["0","1","ABC","DEF","GHI","JKL","MNO","PRS","TUV","WXY"]

number = input("Enter phone number: ")

if number.isnumeric() and len(number) == 7:
   for l1 in letters[int(number[0])]:
      for l2 in letters[int(number[1])]:
         for l3 in letters[int(number[2])]:
            for l4 in letters[int(number[3])]:
               for l5 in letters[int(number[4])]:
                  for l6 in letters[int(number[5])]:
                     for l7 in letters[int(number[6])]:
                        print(f"{l1}{l2}{l3}{l4}{l5}{l6}{l7}")
else:
   print("Invalid input.")