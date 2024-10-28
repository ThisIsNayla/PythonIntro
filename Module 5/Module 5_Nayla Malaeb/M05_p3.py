# Write a program M05_p3.py that asks the user to enter a positive, non-zero integer N and prints the 
# sum of the series: 1 + 1/2 + 1/3 + ... + 1/N. The sum should be displayed using three fractional digits. 
	
# 	Example:  
# 	Please enter the value of N: 100 
# 	The sum of the series is: 5.187 
	
# 	Please enter the value of N: 0 
# 	Invalid input.  
	
# 	Please enter the value of N: fifteen 
#   Invalid input. 

try:
    n = int(input("Please enter the value of N: "))
    if n != 0:
        sum = 0
        for i in range(1,n+1):
            sum = sum + 1/i
        print(f"The sum of the series is: {sum:.3f}")
    else:
        print("Invalid input.")
except:
    print("Invalid input.")
    