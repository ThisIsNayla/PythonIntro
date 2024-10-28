# 	2. Write a program M10_p2.py that asks the user to enter the Cartesian coordinates of three points 
# P1, P2, and P3. The program must check if the three points form the vertices of a triangle 
# (i.e. do not fall on a straight line) and, if they do, calculate its area

# The area of a triangle can be calculated from the Cartesian coordinates of its vertices using the 
# formula: area = 0.5*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)), where abs() is the absolute value 
# function and (x1,y1), (x2,y2), and (x3,y3) are the Cartesian coordinates of P1, P2, and P3, 
# respectively.

# Your program should include two functions isTriangle and calcArea that take three tuple parameters 
# P1, P2, and P3 each. The function isTriangle should return True if the corresponding tuples form the 
# vertices of a triangle and False otherwise. The function calcArea should return the area of the 
# triangle whose vertices are its tuple parameters.

# Examples: 
# Enter x1: 1 
# Enter y2: 2 
# Enter x2: 3 
# Enter y2: 4 
# Enter x3: 5 
# Enter y3: 6 
# The three points are not vertices of a triangle.

# Enter x1: 1 
# Enter y2: 4 
# Enter x2: 3 
# Enter y2: 7 
# Enter x3: 6 
# Enter y3: 4 
# Triangle area = 7.5

def isTriangle(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3

    slope1 = (y2-y1)/(x2-x1)
    slope2 = (y3-y2)/(x3-x2)

    return slope1 == slope2

def calcArea(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    
    area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

    return area

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

P1 = (x1, y1)
P2 = (x2, y2)
P3 = (x3, y3)


if not isTriangle(P1, P2, P3):
    print(f"Triangle area = {calcArea(P1, P2, P3)}")
else:
    print("The three points are not vertices of a triangle.")