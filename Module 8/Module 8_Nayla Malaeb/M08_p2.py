# 	2. The Python module itertools implements a number of iterator functions including the function 
# permutations(), which takes an iterable argument such as a list or a string and returns all permutations
# of that argument. A second, optional argument can also be used to limit the size of the permutations,
# but we will ignore it in this exercise. 

# The permutations() function returns an iterable object which can be accessed by iterating through 
# its elements using a for loop and the in keyword, or by creating a list using the return iterable value. 
# The following is a simple example that generates all permutations of the numbers: 1, 2, and 3. 
# In this example we are creating a list from the result of the permutations() function and assigning 
# it to variable x.

# >>> import itertools
# >>> x = list(itertools.permutations([1,2,3])) 
# >>> print(x) 
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 

# Write a program M08_p2.py that asks the user to enter a word (text string) and prints all permutations
# of that word in capital letters. The program should also print the total number of permutations.

# Example: 
# Please enter word: abc 
# ABC 
# ACB 
# BAC BCA 
# CAB 
# CBA 
# Total permutations = 6 

import itertools

word = input("Please enter word: ")
permutations = list(itertools.permutations(word.upper()))
total_permutations = len(permutations)

for letters in permutations:
    print("".join(letters))

print(f"Total permutations = {total_permutations}")