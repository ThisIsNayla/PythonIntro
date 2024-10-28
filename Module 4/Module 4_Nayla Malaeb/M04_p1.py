# Write a program M04_p1.py that asks the user to enter the value of a restaurant bill and the 
# percentage tip s/he wants to leave. The program should calculate the tip amount and display it in an
# appropriate message. 
	
# The value of the restaurant bill should be entered in the following format: $xx.xx. That is, 
# it should consist of the $ sign followed by a real number expressed using two integer digits and 
# two fractional digits. For example, $25.00 is a valid input. 
	
# Similarly, the value of the tip should be expressed in the following format: xx%. That is, it should 
# consist of a percentage of at most two digits followed by the % sign. For example, 15% and 5% are valid 
# inputs. 
	
# Please use the following code template to write your program.  
	
def main():    
	bill = bill_to_float(input("How much was your bill? "))    
	percent = percent_to_float(input("How much do you want to tip? "))    
	tip = bill * percent    
	print(f"You should leave a ${tip:.2f} tip.")  
	
def bill_to_float(bill):
    return float(bill[1:]) 

def percent_to_float(percent):
    return float(percent[:-1]) / 100

main()

# Coding Style: Notice that the main part of the program is included in a function called main() 
# that is called at the bottom of the program. This coding style ensures that all functions can be 
# called regardless of the order in which they are defined. 
	
# Example: 
# How much was your bill? $25.00 
# How much do you want to tip? 8% 
# You should leave a $2.00 tip. 