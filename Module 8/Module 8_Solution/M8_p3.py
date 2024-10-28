# Program that build a list of prime/non-prime numbers and uses it to check 
# if a given number is prime or not.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

prime = list()

# 0 and 1 are not prime numbers
prime.append(False)
prime.append(False)

# Initialize all list elements to True
for i in range(2,1001,1):
   prime.append(True)

# Check if a list element is divisible by another.      
for i in range(2,1001,1):
   for j in range(i+1,1001,1):
      if j%i == 0:
         prime[j] = False

# Now that we have a list of prime numbers we can check if a number is prime or not
# by looking in the list.
while (True):
   n = int(input("Enter number: "))
   # Entering a negative number ends the program
   if n < 0:
     break
   elif n <= 1000:
      if prime[n]:
         print(f"{n} is a prime number.")
      else:
         print(f"{n} is not a prime number.")
   else:
      print("Invalid input.")
print("Goodbye!")