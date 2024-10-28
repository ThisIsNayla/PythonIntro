# 	3. Write a program M10_p3.py that calculates the probability of a pair of thrown dice having a 
# sum equal to a given number between 2 and 12 after a user-specified number of tries. 
# Your program should ask the user to enter the required sum and the number of dice throws. 
# The program should return the probability of achieving the sum expressed as a percentage. 
# The number of dice throws should be a large number (e.g. 100000) to satisfy the central limit theorem. 
# Your program should use the randint() method and process dice values as tuples.
	
# Example: 
# Enter required sum: 5 
# Enter number of dice throws: 100000 
# Pr(5) = 11.1%

import random
random.seed(1)

from random import randint

try:
    sum = int(input("Enter required sum: "))
    
    count = 0

    if 2 <= sum <= 12:
        tosses = int(input("Enter number of dice throws: "))
        if tosses > 0:
            for toss in range(tosses):
                dice1 = randint(1, 6)
                dice2 = randint(1, 6)
                if dice1 + dice2 == sum:
                    count += 1
            probability = (count/tosses) * 100
            print(f"Pr({sum}) = {probability:.1f}%")
    else:
        print("Invalid sum. Please try again.")
except:
    print("Invalid sum. Please try again.")