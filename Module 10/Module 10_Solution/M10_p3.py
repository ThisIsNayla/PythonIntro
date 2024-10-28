# Program that calculates the probability that the sum of a pair of dice 
# will be equal to a specific sum after a large number of throws.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

import random

def findSum(T):
    return T[0]+T[1]

sum = int(input("Enter required sum: "))
if sum < 2 or sum > 12:
    print("Invalid sum. Please try again.")
else:
    throws = int(input("Enter number of dice throws: "))
    if throws < 1000:
        print("Please use a larger number.")
    else:
        match = 0
        for i in range(throws+1):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            if findSum((dice1, dice2)) == sum:
                match += 1
        prob = (match*100.0)/throws

        print(f"Pr({sum}) = {prob:.1f}%")


