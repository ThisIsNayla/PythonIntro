# Write a program M05_p1.py that asks the user to enter an integer N between 1 and 9 and uses nested loops 
# to display the following pattern: 
	
	# 	1 
	# 	22 
	# 	333 
	# 	4444 
	# 	.... 
	# 	NNNN......N 
		
# Your program must ensure that the user input is valid. Otherwise, it should display an appropriate error 
# message.  
	
# Hint: By default, the print() function automatically inserts a newline character at the end of the 
# displayed string. This causes the display cursor to move to the start of the next line. You can prevent 
# this by adding end="" at the end of the print() function call. 
	# Example: print("No newline", end=""). 
	
	# Example:  
	# Please enter an integer between 1 and 9: 0 
	# Invalid input.  
	
	# Please enter an integer between 1 and 9: four 
	# Invalid input.  
	
	# Please enter an integer between 1 and 9: 3 
	# 1 
	# 22 
    # 333 

try:
    n = int(input("Please enter an integer between 1 and 9: "))
    if n in range(1,10):
        for i in range(1, n+1):
            print(i * str(i), end=" ")
    else:
        print("Invalid input.")
except:
    print("Invalid input.")