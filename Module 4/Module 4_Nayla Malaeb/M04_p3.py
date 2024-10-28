# Rewrite the program M03_p3.py you wrote to convert a score to a letter grade so that it uses a function 
# called calcGrade that takes a single parameter: score. The behavior of the program should otherwise 
# remain unchanged. Save your program as M04_p3.py. 
	
# 	Example:  
# 	Please enter score: failing 
# 	Bad score.  
	
# 	Please enter score: -1.1 
# 	Bad score.  
	
# 	Please enter score: 0.83 
# 	Grade: B  
	
# 	Please enter score: 0.48 
#   Grade: F 

def calcGrade(score):
    try:
        score = float(score)
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

score = input("Please enter score: ")
calcGrade(score)