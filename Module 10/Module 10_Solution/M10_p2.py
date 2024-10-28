# Program that that checks if three points form the vertices of a triangle 
# and, if they do, calculates its area.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

def isTriangle (P1, P2, P3):
   infinity1 = ((P2[0]-P1[0]) == 0)
   infinity2 = ((P3[0]-P2[0]) == 0)
   if not infinity1 and not infinity2:
      slope1 = (P2[1]-P1[1])/(P2[0]-P1[0])
      slope2 = (P3[1]-P2[1])/(P3[0]-P2[0])
      return slope1 != slope2
   elif (not infinity1 and infinity2) or (infinity1 and not infinity2):
      return True
   else:
      return False

def calcArea (P1, P2, P3):
   return 0.5*abs(P1[0]*(P2[1]-P3[1]) + P2[0]*(P3[1]-P1[1]) + P3[0]*(P1[1]-P2[1]))

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

x3 = int(input("Enter x3: "))
y3 = int(input("Enter y3: "))

if isTriangle((x1,y1),(x2,y2),(x3,y3)):
   print(f"Triangle area = {calcArea((x1,y1),(x2,y2),(x3,y3))}")
else:
   print("The three points are not vertices of a triangle.")