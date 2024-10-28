# Write a program (M03_p3.py) that asks the user to enter a score between 0.0 and 1.0. If the score is non-numeric or
# out of range, print an error message. Otherwise, print a grade using the following table:
#
# 		Score 	Grade
# 		>= 0.9 	A
# 		>= 0.8 	B
# 		>= 0.7 	C
# 		>= 0.6 	D
# 		< 0.6 	F
#
# 	Example:
# 	Please enter score: failing
# 	Bad score.
#
# 	Please enter score: -1.1
# 	Bad score.
#
# 	Please enter score: 0.83
# 	Grade: B
#
# 	Please enter score: 0.48
#   Grade: F

try:
    score = float(input("Please enter score: "))
    if 0.9 <= score <= 1.0:
        print("Grade: A")
    elif 0.8 <= score <= 1.0:
        print("Grade: B")
    elif 0.7 <= score <= 1.0:
        print("Grade: C")
    elif 0.6 <= score <= 1.0:
        print("Grade: D")
    elif 0.0 <= score < 0.6:
        print("Grade: F")
    else:
        print("Bad Score.")
except:
    print("Bad Score.")
