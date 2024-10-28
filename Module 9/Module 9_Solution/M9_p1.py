# Program that converts a numeric check value less than or equal to 1000.0 
# into an equivalent text value.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

word_equiv = {0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR", 5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE", 10:"TEN", 11:"ELEVEN", 12:"TWELVE", 13:"THIRTEEN", 14:"FOURTEEN", 15:"FIFTEEN", 16:"SIXTEEN", 17:"SEVENTEEN", 18:"EIGHTEEN", 19:"NINETEEN", 20:"TWENTY", 30:"THIRTY", 40:"FORTY", 50:"FIFTY", 60:"SIXTY", 70:"SEVENTY", 80:"EIGHTY", 90:"NINETY"}

try:
   value = float(input("Enter check value: "))
   if value > 1000.0 or value < 0.0:
      print("Invalid input.")
   else:
      if value == 1000.00:
         print("ONE THOUSAND AND 00/100")
      else:
         hundreds = int(value//100)
         if hundreds != 0:
            print(f"{word_equiv[hundreds]} HUNDRED ",end="")
         tens = int(value % 100)
         if tens > 0 and tens < 20:
            print(f"{word_equiv[tens]} ",end="")
         else:
            if tens > 0:
               tens = (tens//10)*10
               print(f"{word_equiv[tens]} ",end="")
            ones = int(value % 10)
            if (ones > 0 and ones < 10) or (ones == 0 and tens == 0 and hundreds == 0):
               print(f"{word_equiv[ones]} ",end="")
         frac = int((round(value * 100))%100)
         print(f"AND {frac:02d}/100")
except:
   print("Invalid input.")

