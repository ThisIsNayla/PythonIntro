# 	1. Write a program that checks if three points P1, P2, and P3 with Cartesian coordinates (x1,y1), 
# (x2,y2), and (x3,y3), respectively, fall on a straight line. One way to do this is to check if the 
# slope of P1 and P2 is equal to the slope of P2 and P3. The slope of a pair of points T and U with 
# Cartesian coordinates (a, b) and (c, d) can be calculated using the formula: s = (d-b)/(c-a).
	
# Write a program M10_p1.py that asks the user to enter three pairs of Cartesian coordinates and checks 
# if they fall on a straight line. Your program must store the three coordinate pairs as tuples. 
# The code for checking the three coordinates should be implemented as a function onStraightLine 
# that takes three tuple parameters P1, P2, and P3, and returns True or False.

# Examples:
# Enter x1: 1 
# Enter y2: 2 
# Enter x2: 3 
# Enter y2: 4 
# Enter x3: 5 
# Enter y3: 6 
# The three points are on a straight line.

# Enter x1: 1 
# Enter y2: 2 
# Enter x2: 3 
# Enter y2: 4 
# Enter x3: -10 
# Enter y3: 15 
# The three points are not on a straight line.

def onStraightLine(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    slope1 = (y2-y1)/(x2-x1)
    slope2 = (y3-y2)/(x3-x2)

    return slope1 == slope2

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

P1 = (x1, y1)
P2 = (x2, y2)
P3 = (x3, y3)

if onStraightLine(P1, P2, P3):
    print("The three points are on a straight line.")
else:
    print("The three points are not on a straight line.")