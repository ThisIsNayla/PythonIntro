# 1.   Standard telephone keypads contain the digits 0 through 9. Each of the numbers 2 through 9 have three
# letters associated with them, as shown in the following table:
		
# 		Digit 	Letters 
# 		2 	ABC
# 		3 	DEF
# 		4 	GHI 
# 		5 	JKL 
# 		6 	MNO 
# 		7 	PRS 
# 		8 	TUV 
# 		9 	WXY
		
# Many people find it difficult to memorize phone numbers, so they use the digit-to-letter mapping to 
# create seven-letter words that correspond to their phone numbers. For example, a data science company 
# might want to reserve the phone number 244-3282 because it maps to the word: "BIGDATA". Note that every 
# seven-letter word or phrase maps to exactly one seven-digit telephone number, while every seven-digit 
# phone number (without 0’s or 1’s) can map to many possible seven-letter words even though most of these 
# words are meaningless. 

# Write a program M08_p1.py that asks a user to enter a seven-digit number without any hyphens or other 
# punctuation marks, and generates every possible seven-letter word combination corresponding to that number.
# If the number does not contain 0’s or 1’s, there are 2,187 (37 ) such combinations. If a number contains
# the digits 0 or 1, they should be included unchanged in the generated words (e.g. AB0CD1E).

# Example: 
# Please enter phone number: 244-3282 
# Invalid input.

# Please enter phone number: 2443282 
# AGGDATA 
# AGGDATB 
# ... 
# BIGDATA 
# ... 
# CIIFCVC

# Please enter phone number: 
# 2440000 
# AGG0000 
# AGH0000 
# ... 
# CII0000 

phone_number = input("Please enter phone number: ")

if phone_number.isdigit() and len(phone_number) == 7:
    keypad = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PRS", "TUV", "WXY"]

    combinations = [""]

    for digit in phone_number:
        if digit == "0" or digit == "1":
            combinations = [element + digit for element in combinations]
        else:
            new_combinations = []
            for element in combinations:
                for letter in keypad[int(digit)]:
                    new_combinations.append(element + letter)
            combinations = new_combinations

    for word in combinations:
        print(word)

else:
    print("Invalid input.")