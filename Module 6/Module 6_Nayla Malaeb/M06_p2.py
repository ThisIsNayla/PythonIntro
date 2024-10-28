# Write a program M06_p2.py that asks the user to enter a password and verifies that it contains at 
# least 8 characters, an uppercase letter, a lowercase letter, a number, and a special character from 
# the set: !"#$%&'()*+,-./:;<=>?@[\]^_`{} . Your program must then report the length of the password 
# and the number of characters that satisfy each criterion. If a password does not meet a certain 
# criterion a (*) should be displayed next to that criterion. The program should end by reporting 
# whether the password has PASSED or FAILED.  
# Note: To distinguish double quotes (") from the start or end of a string, you should refer to it 
# using the \" character. 
	
# 	Example:   
# 	Enter password: pa$$word 
# 	Password length: 8 
# 	Uppercase letters: 0 (*) 
# 	Lowercase letters: 6 
# 	Numbers: 0 (*) 
# 	Special characters: 2 
# 	Status: FAILED  
	
# 	Enter password: P@$$word1 
# 	Password length: 9 
# 	Uppercase letters: 1 
# 	Lowercase letters: 4 
# 	Numbers: 1 
# 	Special characters: 3 
# 	Status: PASSED  

password = str(input("Enter password: "))

special = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{}"

password_length = len(password)
upper_count = 0
lower_count = 0
num_count = 0
special_count = 0

for char in password:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        num_count += 1
    elif char in special:
        special_count += 1

print(f"Password length: {password_length} {"(*)" if password_length < 8 else ""}")
print(f"Uppercase letters: {upper_count} {"(*)" if upper_count == 0 else ""}")
print(f"Lowercase letters: {lower_count} {"(*)" if lower_count == 0 else ""}")
print(f"Numbers: {num_count} {"(*)" if num_count == 0 else ""}")
print(f"Special characters: {special_count} {"(*)" if special_count == 0 else ""}")

if password_length >= 8 and upper_count != 0 and lower_count != 0 and num_count != 0 and special_count != 0:
    print("Status: PASSED")
else:
    print("Status: FAILED")