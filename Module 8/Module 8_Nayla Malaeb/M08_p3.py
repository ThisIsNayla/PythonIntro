# 	3. Write a program M08_p3.py that checks if a number less than 1000 is prime or not. Recall that a prime
# number is divisible by 1 and itself. 
	
# Start by creating a 1000-element list and initialize its elements to True. Next, scan all elements i 
# from 2 to 1000. For each element, scan all elements j from i+1 to 1000. If j is a multiple of i, set the 
# corresponding list element to False. Finally, set list elements 0 and 1 to False.

# Next, ask the user to enter a number, and use the list to determine if the number is prime or not through 
# a simple look-up operation. Your program should continue to check numbers until the user enters a negative 
# number.

# Example:
# Enter a number: 5 
# 5 is a prime number. 

# Enter a number: 18 
# 18 is not a prime number. 

# Enter a number: 0 
# 0 is not a prime number. 

# Enter a number: -1 Goodbye!

numbers = [True] * 1001
numbers[0] = False
numbers[1] = False

for i in range(2, 1001):
    if numbers[i]:
    	for j in range(i + 1, 1001):
            if j % i == 0:
                numbers[j] = False
            
while True:
     number = int(input("Enter a number: "))
     if number < 0:
        print("Goodbye!")
        break
     elif numbers[number]:
         print(f"{number} is a prime number.")
     else: 
         print(f"{number} is not a prime number.")