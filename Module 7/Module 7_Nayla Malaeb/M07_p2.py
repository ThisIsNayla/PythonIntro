# A comma-separated values (CSV) file is a text file that uses commas to separate its data values. 
# Each line of a CSV file corresponds to a single data record. Each record consists of one or more fields
# that are separated by commas. CSV files have become a common data format and are used by application
# programs like Microsoft Excel. 
	
# Write a program M07_p2.py that asks a user to enter student records consisting of a student's last name,
# first name, and three exam grades. In addition to the user-supplied data, the program should calculate
# the student's average grade as a whole integer and the corresponding letter grade based on the 
# following table:

# Numerical	Letter
# >= 90	    A
# >= 80 	B
# >= 70 	C
# >= 60 	D
# <60 	    F

# Each student record should be saved to CSV file grades.csv. The program should continue asking for 
# student data until the user enters an empty last name. Re-running the program should enable new records 
# to be appended to grades.csv.

# Example:
# Enter student's last name: Anderson
# Enter student's first name: Alice
# Enter exam 1 grade: 83
# Enter exam 2 grade: 92
# Enter exam 3 grade: 96

# grades.csv entry:

# Anderson,Alice,83,92,96,90,A

last_name = input("Enter student's last name: ")
first_name = input("Enter student's first name: ")
exam1 = int(input("Enter exam 1 grade: "))
exam2 = int(input("Enter exam 2 grade: "))
exam3 = int(input("Enter exam 3 grade: "))

average = int((exam1 + exam2 + exam3) / 3)

if average >= 90:
    letter = "A"
elif average >= 80:
    letter = "B"
elif average >= 70:
    letter = "C"
elif average >= 60:
    letter = "D"
elif average < 60:
    letter = "f"

with open("grades.csv", "w") as file:
    file.write(f"{last_name},{first_name},{exam1},{exam2},{exam3},{average},{letter}")