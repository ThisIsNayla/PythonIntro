# 	1. A common method of increasing the security of check-writing systems is to write the value of 
# a check in words. Write a program M9_p1.py that uses a dictionary to map numbers to their 
# corresponding word equivalents. Your program should ask the user to enter a check value that is 
# less than $1000.0 and use the dictionary to produce the text equivalent of the check value.
	
# Example:
# Enter check value: 2000 
# Invalid input. 

# Enter check value: -100 
# Invalid input. 

# Enter check value: 154.30 
# ONE HUNDRED FIFTY FOUR AND 30/100 

# Enter check value: 603.25 
# SIX HUNDRED THREE AND 25/100

ones = {
    0: "ZERO",
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR",
    5: "FIVE",
    6: "SIX",
    7: "SEVEN",
    8: "EIGHT",
    9: "NINE"
}

teens = {
    10: "TEN",
    11: "ELEVEN",
    12: "TWELVE",
    13: "THIRTEEN",
    14: "FOURTEEN",
    15: "FIFTEEN",
    16: "SIXTEEN",
    17: "SEVENTEEN",
    18: "EIGHTEEN",
    19: "NINETEEN"
}

tens = {
    2: "TWENTY",
    3: "THIRTY",
    4: "FORTY",
    5: "FIFTY",
    6: "SIXTY",
    7: "SEVENTY",
    8: "EIGHTY",
    9: "NINETY"
}

hundreds = ones.copy()
for i in range(1, len(ones)):
    hundreds[i] = ones[i] + " HUNDRED"
del hundreds[0]

number = float(input("Enter check value: "))

if 0 <= number < 1000:
    words = []

    if number >= 100:
        words.append(hundreds[int(number // 100)])
        number %= 100

    if number >= 20:
        words.append(tens[int(number // 10)])
        number %= 10
            
    elif number >= 10:
        words.append(teens[int(number)])
        
    if 10 > number >= 0:
        words.append(ones[int(number)])
        
    decimal_part = "{:.2f}".format(number % 1)
    words.append("AND " + decimal_part[2:] + "/100")

    print(" ".join(words))
	
else:
    print("Invalid input.")