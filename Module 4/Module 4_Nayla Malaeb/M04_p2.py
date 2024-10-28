# Rewrite the program M03_p1.py that calculates wages while taking overtime hours into consideration 
# so that it uses a function called calcPay that takes two parameters: hours and rate. The behavior of the 
# program should otherwise remain unchanged. Save your program as M04_p2.py. 
	
	# Example:  
	# Please enter hourly wage: 6 
	# Please enter hours worked: 40 
	# Total wages = 240.0  
	
	# Please enter hourly wage: 6 
	# Please enter hours worked: 50 
    # Total wages = 330.0

def calcPay(hours, rate):
    total = rate * hours
    if total > 40:
        extra_hours = (1.5 * rate) * (hours - 40)
        total = (40 * rate) + extra_hours
    print("Total wages =", total)

rate = float(input("Please enter hourly wage: "))
hours = float(input("Please enter hours worked: "))
calcPay(hours, rate)