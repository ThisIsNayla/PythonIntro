# Program that that checks if three pairs of Cartesian coordinates 
# fall on a straight line. 
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

def onStraightLine (P1, P2, P3):
   # If the points have the same x-coordinates they fall on a straight line.
   if (P2[0]-P1[0] == 0) and (P3[0]-P2[0] == 0):
      return True
   else:
      slope1 = (P2[1]-P1[1])/(P2[0]-P1[0])
      slope2 = (P3[1]-P2[1])/(P3[0]-P2[0])
      return slope1 == slope2

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

# Coordinates are passed as tuple arguments
if onStraightLine((x1,y1),(x2,y2),(x3,y3)):
   print("The three points are on a straight line.")
else:
   print("The three points are not on a straight line.")