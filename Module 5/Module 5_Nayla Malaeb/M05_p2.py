# Write a program M05_p2.py that asks the user to enter positive integer lower and upper bounds and
# the letter 'o' (odd) or 'e' (even) in lowercase. Depending on the input, use a while loop to add
# up all the odd/even numbers between the lower and upper bounds, and display the result in an
# appropriate message. If the user enters an invalid input, or if the upper bound is less than the
# lower bound, your program must display an error message.  
	
# 	Example:  
# 	Enter lower bound: 0 
# 	Enter upper bound: 10 
# 	Even or odd? e 
# 	The sum of even numbers between 0 and 10 is: 30 
	
# 	Enter lower bound: 10 
# 	Enter upper bound: 0 
# 	Even or odd? e 
# 	Invalid input. 
	
# 	Enter lower bound: 0 
# 	Enter upper bound: 10 
# 	Even or odd? ODD 
# 	Invalid input. 

lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
e_o = str(input("Even or odd? "))

if lower < upper and (e_o == "e" or e_o == "o"):
    sum = 0
    i = lower + 1
    while i <= upper:
        if e_o == "e" and i%2 == 0:
            sum = sum + i
            answer = 'even'
        elif e_o == "o" and i%2 != 0:
            sum = sum + i
            answer = 'odd'
        i = i + 1
    print(f"The sum of {answer} numbers between {lower} and {upper} is: {sum}")
else:
    print("Invalid input.")