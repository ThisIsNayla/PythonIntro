# PythonIntro

## Module 2 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 2 (Variables, Expressions, and Statements) and develop your coding skills. 

**Instructions**

1. Write a program **M02_p1.py** that asks a user to enter the year of her/his birth and prints the user's age.

**Example:**

```
Please enter the year of your birth: 1995
You are 27 years old.
```

2. Write a program **M02_p2.py** that asks a user to enter a weight in kilograms (kg) and converts it to pounds (lbs). Note that there are 2.2 lbs per kg.

**Example:**
```
Please enter the weight in kg: 45.6
Weight = 100.32 lbs.
```

3. Write a program **M02_p3.py** that asks a user to enter their hourly wage and number of hours worked and calculates the user's wages.

**Example:**
```
Please enter hourly wage: 5.75
Please enter hours worked: 40
Total wages = 230.0
```

## Module 3 Coding Assignment

**Purpose**
The purpose of this activity is to consolidate material from Module 3 (Conditional Execution) and develop your coding skills.

**Instructions**

1. Write a program **M03_p1.py** that updates the wages program you wrote for your Module 2 assignment (**M02_p3.py**). In addition to asking the user to enter their hourly wage and number of hours worked, your program must calculate the total wages using 1.5 times the hourly wage for work done beyond 40 hours.

**Example:**
```
Please enter hourly wage: 6
Please enter hours worked: 40
Total wages = 240.0
Please enter hourly wage: 6
Please enter hours worked: 50
Total wages = 330.0
```

2. Modify **M03_p1.py** to use try-except to catch non-numeric input. Save your program as **M03_p2.py**.

**Example:**
```
Please enter hourly wage: six
Invalid input. Please use numeric values.

Please enter hourly wage: 6
Please enter hours worked: fifty
Invalid input. Please use numeric values.

Please enter hourly wage: 6
Please enter hours worked: 50
Total wages = 330.0
```

3. Write a program (M03_p3.py) that asks the user to enter a score between 0.0 and 1.0. If the score is non-numeric or out of range, print an error message. Otherwise, print a grade using the following table:

    Score     Grade
    >= 0.9     A
    >= 0.8     B
    >= 0.7     C
    >= 0.6     D
    < 0.6      F

**Example:**
```
Please enter score: failing
Bad score.

Please enter score: -1.1
Bad score.

Please enter score: 0.83
Grade: B

Please enter score: 0.48
Grade: F
```

## Module 4 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 4 (Functions) and develop your coding skills. 

**Instructions**

1. Write a program **M04_p1.py** that asks the user to enter the value of a restaurant bill and the percentage tip s/he wants to leave. The program should calculate the tip amount and display it in an appropriate message.

The value of the restaurant bill should be entered in the following format: $xx.xx. That is, it should consist of the $ sign followed by a real number expressed using two integer digits and two fractional digits. For example, $25.00 is a valid input.

Similarly, the value of the tip should be expressed in the following format: xx%. That is, it should consist of a percentage of at most two digits followed by the % sign. For example, 15% and 5% are valid inputs.

Please use the following code template to write your program. 

```
def main():
 bill = bill_to_float(input(“How much was your bill? ”))
 percent = percent_to_float(input(“How much do you want to tip? ”))
 tip = bill * percent
 print(“You should leave a ${tip:.2f} tip.”)

def bill_to_float(b):
 # Add your code here

def percent_to_float(p):
 # Add your code here

main()
```

**Coding Style**: Notice that the main part of the program is included in a function called `main()` that is called at the bottom of the program. This coding style ensures that all functions can be called regardless of the order in which they are defined.

**Example:**
```
How much was your bill? $25.00
How much do you want to tip? 8%
You should leave a $2.00 tip.
```

2. Rewrite the program **M03_p1.py** that calculates wages while taking overtime hours into consideration so that it uses a function called **calcPay** that takes two parameters: hours and rate. The behavior of the program should otherwise remain unchanged. Save your program as **M04_p2.py**.

**Example:**
```
Please enter hourly wage: 6
Please enter hours worked: 40
Total wages = 240.0

Please enter hourly wage: 6
Please enter hours worked: 50
Total wages = 330.0
```

3. Rewrite the program **M03_p3.py** you wrote to convert a score to a letter grade so that it uses a function called **calcGrade** that takes a single parameter: score. The behavior of the program should otherwise remain unchanged. Save your program as **M04_p3.py**.

**Example:**
```
Please enter score: failing
Bad score.
Please enter score: -1.1
Bad score.
Please enter score: 0.83
Grade: B
Please enter score: 0.48
Grade: F
```

## Module 5 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 5 (Iteration) and develop your coding skills.   

**Instructions**

1. Write a program **M05_p1.py** that asks the user to enter an integer N between 1 and 9 and uses nested loops to display the following pattern:
```
1
22
333
4444
....
NNNN......N
```

Your program must ensure that the user input is valid. Otherwise, it should display an appropriate error message.

**Hint**: By default, the `print()` function automatically inserts a newline character at the end of the displayed string. This causes the display cursor to move to the start of the next line. You can prevent this by adding `end=""` at the end of the `print()` function call. Example: `print("No newline",end="")`.

**Example:**
```
Please enter an integer between 1 and 9: 0
Invalid input.

Please enter an integer between 1 and 9: four
Invalid input.

Please enter an integer between 1 and 9: 3
1
22
333
```

2. Write a program **M05_p2.py** that asks the user to enter positive integer lower and upper bounds and the letter 'o' (odd) or 'e' (even) in lowercase. Depending on the input, use a while loop to add up all the odd/even numbers between the lower and upper bounds, and display the result in an appropriate message. If the user enters an invalid input, or if the upper bound is less than the lower bound, your program must display an error message.

**Example:**
```
Enter lower bound: 0
Enter upper bound: 10
Even or odd? e
The sum of even numbers between 0 and 10 is: 30

Enter lower bound: 10
Enter upper bound: 0
Even or odd? e
Invalid input.

Enter lower bound: 0
Enter upper bound: 10
Even or odd? ODD
Invalid input.
```

3. Write a program **M05_p3.py** that asks the user to enter a positive, non-zero integer N and prints the sum of the series: 1 + 1/2 + 1/3 + ... + 1/N. The sum should be displayed using three fractional digits.

**Example:**
```
Please enter the value of N: 100
The sum of the series is: 5.187

Please enter the value of N: 0
Invalid input.

Please enter the value of N: fifteen
invalid input.
```

## Module 6 Coding Assignment

**Purpose**
The purpose of this activity is to consolidate material from Module 6 (Strings) and develop your coding skills. 

**Instructions**

1. In cryptography, the Caesar cipher is a simple and widely used encryption technique. It is a type of substitution cipher in which each letter of an input plaintext is replaced by a letter that is at a fixed number of positions up or down the alphabet. For example, with a left shift of 3, the letter 'D' would be replaced by an 'A'; the letter 'E' would become a 'B', and so on.

The transformation can be represented by aligning two alphabets; the plain alphabet and the cipher alphabet, which is the plain alphabet rotated left or right by some number of positions. For example, here is a Caesar cipher using a left rotation of three characters, which is equivalent to a right shift of 23 characters: 

<img width="639" alt="Screenshot 2024-10-28 at 12 25 50" src="https://github.com/user-attachments/assets/d29cc6ac-b6f3-46bf-a8b8-c9a8f66c0f13">

Using this cipher, the plaintext: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG becomes the ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD.

Caesar cipher encryption can be represented using modular arithmetic by first transforming letters into numbers according to the scheme: A = 0, B = 1, ... Z = 25. Encrypting a letter x rotated by n characters can be described mathematically as: En(x) = (x + n) % 26.

In Python, a character can be converted to its UTF-8 code using the ord() function. Conversely, the character for a given UTF-8 code can be generated using the chr() function. For example, `ord('a')` = 97 and `chr(97)` = 'a'. Moreover, expressions like `ord('d') - ord('a')` return the difference in the number of characters between 'a' and 'd'.

Write a program **M06_p1.py** that asks the user to enter a plaintext and a rotation value, and that returns the corresponding Ceasar cipher ciphertext. The rotation value can be any positive or negative integer, and the plaintext may include lowercase, uppercase, or nonalphabetic characters (e.g. punctuation marks, white space, and digits). A negative rotation value corresponds to a left rotation, and a positive rotation value corresponds to a right rotation.

Your program should use a function rotateString that takes two parameters: `instr` and `rot`, which correspond to the input plaintext and rotation value, respectively. The function should return the ciphertext string.

**Example:**
```
Enter plaintext: Hello, world!
Enter rotation value: -2
Ciphertext: Fcjjm, umpjb!
```

2. Write a program **M06_p2.py** that asks the user to enter a password and verifies that it contains at least 8 characters, an uppercase letter, a lowercase letter, a number, and a special character from the set: !"#$%&'()`*`+,-./:;<=>?@[\]^_`{} . Your program must then report the length of the password and the number of characters that satisfy each criterion. If a password does not meet a certain criterion a (*) should be displayed next to that criterion. The program
should end by reporting whether the password has PASSED or FAILED.

Note: To distinguish double quotes (") from the start or end of a string, you should refer to it using the \" character.

**Example:**
```
Enter password: pa$$word
Password length: 8
Uppercase letters: 0 (*)
Lowercase letters: 6
Numbers: 0 (*)
Special characters: 2
Status: FAILED

Enter password: P@$$word1
Password length: 9
Uppercase letters: 1
Lowercase letters: 4
Numbers: 1
Special characters: 3
Status: PASSED 
```

3. A palindrome is a word that reads the same from either end. For example, "civic", "radar", and "madam" are palindromes, while "tree", "car", and "horse" are not. Write a program **M06_p3.py** that asks the user to enter a word and checks if the word is a palindrome. Note that single-letter words are allowed and should be considered palindromes.

**Example:**
```
Enter a word: civic
civic is a palindrome.
Enter a word: tree
tree is not a palindrome.
```

## Module 7 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 7 (Files) and develop your coding skills.   

**Instructions**

1. Write a program **M07_p1.py** that asks the user to enter the name of a text file and a word size. The program should print all words in the file that have that size and return the total number of words that match the size in an appropriate message. Except for apostrophes, punctuation marks that belong to the string: ",.;:?" should not be counted as part of the word length. For example, "day?" should be counted as a three-letter word and "wand'rest" should be counted as a 9 letter word. To help you develop your program, a text file (sonnet18.txt) containing Shakespeare's Sonnet 18 will be provided for you.

**Example:**
```
Enter file name: sonnet18.txt
Enter word length: 9
temperate
untrimmed
wand'rest
Total words of length 9: 3 
```

2. A comma-separated values (CSV) file is a text file that uses commas to separate its data values. Each line of a CSV file corresponds to a single data record. Each record consists of one or more fields that are separated by commas. CSV files have become a common data format and are used by application programs like Microsoft Excel.

Write a program **M07_p2.py** that asks a user to enter student records consisting of a student's last name, first name, and three exam grades. In addition to the user-supplied data, the program should calculate the student's average grade as a whole integer and the corresponding letter grade based on the following table:

  Numerical    Letter
  >= 90          A
  >= 80          B
  >= 70          C
  >= 60          D
  <60            F

Each student record should be saved to CSV file grades.csv. The program should continue asking for student data until the user enters an empty last name. Re-running the program should enable new records to be appended to grades.csv.

**Example:**
```
Enter student's last name: Anderson
Enter student's first name: Alice
Enter exam 1 grade: 83
Enter exam 2 grade: 92
Enter exam 3 grade: 96

grades.csv entry:
Anderson,Alice,83,92,96,90,A 
```

## Module 8 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 8 (Lists) and develop your coding skills. 

Instructions
1. Standard telephone keypads contain the digits 0 through 9. Each of the numbers 2 through 9 have three letters associated with them, as shown in the following table:
    Digit     Letters
      2         ABC
      3         DEF
      4         GHI
      5         JKL
      6         MNO
      7         PRS
      8         TUV
      9         WXY

Many people find it difficult to memorize phone numbers, so they use the digit-to-letter mapping to create seven-letter words that correspond to their phone numbers. For example, a data science company might want to reserve the phone number 244-3282 because it maps to the word: "BIGDATA". Note that every seven-letter word or phrase maps to exactly one seven-digit telephone number, while every seven-digit phone number (without 0’s or 1’s) can map to many possible seven-letter words even though most of these words are meaningless.

Write a program **M08_p1.py** that asks a user to enter a seven-digit number without any hyphens or other punctuation marks, and generates every possible seven-letter word combination corresponding to that number. If the number does not contain 0’s or 1’s, there are 2,187 (37) such combinations. If a number contains the digits 0 or 1, they should be included unchanged in the generated words (e.g. AB0CD1E).

**Example:**
```
Please enter phone number: 244-3282
Invalid input.

Please enter phone number: 2443282
AGGDATA
AGGDATB
...
BIGDATA
...
CIIFCVC

Please enter phone number: 2440000
AGG0000
AGH0000
...
CII0000
```

2. The Python module **itertools** implements a number of iterator functions including the function **permutations()**, which takes an iterable argument such as a list or a string and returns all permutations of that argument. A second, optional argument can also be used to limit the size of the permutations, but we will ignore it in this exercise.

The **permutations()** function returns an iterable object which can be accessed by iterating through its elements using a **for** loop and the **in** keyword, or by creating a list using the return iterable value. The following is a simple example that generates all permutations of the numbers: 1, 2, and 3. In this example we are creating a list from the result of the **permutations()** function and assigning it to variable x.

```
>>> import itertools
>>> x = list(itertools.permutations([1,2,3]))
>>> print(x)
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] 
```

Write a program **M08_p2.py** that asks the user to enter a word (text string) and prints all permutations of that word in capital letters. The program should also print the total number of permutations.

**Example:**
```
Please enter word: abc
ABC
ACB
BAC
BCA
CAB
CBA
Total permutations = 6
```

3. Write a program M08_p3.py that checks if a number less than 1000 is prime or not. Recall that a prime number is divisible by 1 and itself.

Start by creating a 1000-element list and initialize its elements to True. Next, scan all elements i from 2 to 1000. For each element, scan all elements j from i+1 to 1000. If j is a multiple of i, set the corresponding list element to False. Finally, set list elements 0 and 1 to False.

Next, ask the user to enter a number, and use the list to determine if the number is prime or not through a simple look-up operation. Your program should continue to check numbers until the user enters a negative number.

**Example:**
```
Enter a number: 5
5 is a prime number.
Enter a number: 18
18 is not a prime number.
Enter a number: 0
0 is not a prime number.
Enter a number: -1
Goodbye!
```

## Module 9 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 9 (Dictionaries) and develop your coding skills. 

**Instructions**

1. A common method of increasing the security of check-writing systems is to write the value of a check in words. Write a program M9_p1.py that uses a dictionary to map numbers to their corresponding word equivalents. Your program should ask the user to enter a check value that is less than $1000.0 and use the dictionary to produce the text equivalent of the check value.

**Example:**
```
Enter check value: 2000
Invalid input.

Enter check value: -100
Invalid input.

Enter check value: 154.30
ONE HUNDRED FIFTY FOUR AND 30/100

Enter check value: 603.25
SIX HUNDRED THREE AND 25/100
```

2. Write a program **M9_p2.py** that reads a user-specified text file and uses a dictionary to print all duplicate words in the file and their corresponding counts. A word is a duplicate if it appears more than once in the file. Your program should not consider punctuation marks (,.;?!:) to be part of a word. It should also treat words in uppercase or lowercase letters as being the same. For example, the words "The" and "the" should be treated as being identical. Use the sorted() function to sort the dictionary alphabetically before printing duplicate words.

**Example:**
```
Enter file name: sonnet18.txt
Duplicate words:
a 2
and 5
can 2
eternal 2
...
```

3. The file **temperatures.txt** contains temperature readings over a 24-hour period. The first line contains a date, and the remaining 24 lines contain the time expressed in 24-hour format and the corresponding measured temperature separated by a comma.

Write a program **M9_p3.py** that reads **temperatures.txt** and prints the date and the minimum, maximum, and average temperatures. Your program must use a dictionary. The minimum temperature should be calculated from temperatures gathered from 0:00 to 06:00 and 20:00 to 23:00, respectively. The maximum temperature should be calculated from temperatures gathered from 7:00 to 19:00. A sample **temperatures.txt** file is provided on the course web site for reference.

**Example:**
```
Sunday, July 10, 2022
Temp. Low = 24.0
Temp. High = 30.0
Temp. Avg. = 26.7
```

## Module 10 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 10 (Tuples) and develop your coding skills.   

**Instructions**

1. Write a program that checks if three points P1, P2, and P3 with Cartesian coordinates (x1,y1), (x2,y2), and (x3,y3), respectively, fall on a straight line. One way to do this is to check if the slope of P1 and P2 is equal to the slope of P2 and P3. The slope of a pair of points T and U with Cartesian coordinates (a, b) and (c, d) can be calculated using the formula: s = (d-b)/(c-a).

Write a program **M10_p1.py** that asks the user to enter three pairs of Cartesian coordinates and checks if they fall on a straight line. Your program must store the three coordinate pairs as tuples. The code for checking the three coordinates should be implemented as a function onStraightLine that takes three tuple parameters P1, P2, and P3, and returns True or False

**Examples:**
```
Enter x1: 1
Enter y2: 2
Enter x2: 3
Enter y2: 4
Enter x3: 5
Enter y3: 6
The three points are on a straight line.

Enter x1: 1
Enter y2: 2
Enter x2: 3
Enter y2: 4
Enter x3: -10
Enter y3: 15
The three points are not on a straight line.
```

2. Write a program **M10_p2.py** that asks the user to enter the Cartesian coordinates of three points P1, P2, and P3. The program must check if the three points form the vertices of a triangle (i.e. do not fall on a straight line) and, if they do, calculate its area.

The area of a triangle can be calculated from the Cartesian coordinates of its vertices using the formula: area = 0.5*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)), where abs() is the absolute value function and (x1,y1), (x2,y2), and (x3,y3) are the Cartesian coordinates of P1, P2, and P3, respectively.

Your program should include two functions **isTriangle** and **calcArea** that take three tuple parameters P1, P2, and P3 each. The function **isTriangle** should return True if the  corresponding tuples form the vertices of a triangle and False otherwise. The function **calcArea** should return the area of the triangle whose vertices are its tuple parameters.

**Examples:**
```
Enter x1: 1
Enter y2: 2
Enter x2: 3
Enter y2: 4
Enter x3: 5
Enter y3: 6
The three points are not vertices of a triangle.

Enter x1: 1
Enter y2: 4
Enter x2: 3
Enter y2: 7
Enter x3: 6
Enter y3: 4
Triangle area = 7.5
```

3. Write a program **M10_p3.py** that calculates the probability of a pair of thrown dice having a sum equal to a given number between 2 and 12 after a user-specified number of tries. Your program should ask the user to enter the required sum and the number of dice throws. The program should return the probability of achieving the sum expressed as a percentage. The number of dice throws should be a large number (e.g. 100000) to satisfy the central limit theorem. Your program should use the **randint()** method and process dice values as tuples.

**Example:**
```
Enter required sum: 5
Enter number of dice throws: 100000
Pr(5) = 11.1%
```

## Module 11 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 11 (Networked Programs) and develop your coding skills.   

**Instructions**

1. The file **romeo-full.txt** contains Act 2, Scene 2 from William Shakespeare's Romeo and Juliet. Write a program **M11_p1.p**y that uses sockets to read **romeo-full.txt** from the server **data.pr4e.org** and saves it on your computer. Be sure to only save the contents of the file after removing the HTTP header. Use the Module 11 slides as a reference and remember that data is transferred across a network as bytes. **Hint**: You will need to use the **decode()** string method.

2. Write a program **M11_p2.py** that uses sockets to read romeo-full.txt from **data.pr4e.org** and prints the 10 most frequent words in the text. You can use techniques you learned in earlier modules, but you must not save the file on your computer. You must also clean the text before counting its words by replacing hyphens with spaces, and the character sequence apostrophe-s-space with a single space (i.e. replace "Romeo's " with "Romeo "). Use the Module 11 slides as a reference and remember that data is transferred across a network as bytes. **Hint**: To access a tuple element in a list of tuples (L) use the tuple index, t, and the tuple element index, e: L[t][e]. Example: if L = [('a',1), ('b',2), ('c',3)], L[2][1] returns 3 and L[1][0] returns 'b'.

3. Repeat question 2 using **urllib**. Use the Module 11 slides as reference and save your program **as M11_p3.py**.

## Module 12 Coding Assignment

**Purpose**

The purpose of this activity is to consolidate material from Module 12 (Using Web Services) and develop your coding skills.   

**Instructions**

1. In the Module 12 slides, we learned how to process XML data that was entered as a string using the triple quotes operator. However, it is more common to read XML data stored in a file.

Python's **xml.etree.ElementTree** module includes a **parse()** function that takes the name of an XML file as an argument and returns a corresponding parse tree. A parse tree is a data structure that Python uses to find data stored in XML format. The **getroot()** function returns the root of the tree, which represents the starting point for extracting data using the **find()** function.
The following shows how to print the data from the multiple XML node example assuming the data is stored in the file "data.xml". Study this code and compare it to the code in the slides. A copy of "data.xml" is available on the course web site for reference.

```
import xml.etree.ElementTree as ET

tree = ET.parse("data.xml")
stuff = tree.getroot()

lst = stuff.findall("users/user")
print("User count:", len(lst))
for item in lst:
 print("Name:", item.find("name").text)
 print("Id:",item.find("id").text)
 print("Attribute:",item.get("x"))
```

Now that you have learned how to extract data from an XML file, we will look at a problem that data scientists encounter daily. The XML file "europe.xml" contains data on 50 European countries. In addition to a country's name, the data includes its area (in km2), capital city, population, and gross domestic product (GDP) per capita in US dollars.

Write a Python program **M12_p1.py** that reads the XML file and prints the top 10 European economies and highest population densities, respectively. A country's economy is reported in billions of US dollars and is the product of the GDP per capita by the population size. A country's population density is the quotient of the population by the area. All results should be reported to a precision of two decimal points.

**Example:**
```
Top 10 Economies in Europe:
<country1>: <size of the 1st largest economy in billions of US dollars>
<country2>: <size of the 2nd largest economy in billions of US dollars>
<country3>: <size of the 3rd largest economy in billions of US dollars>
...
Top 10 Population Densities in Europe:
<country1>: <1st largest population density in persons/km2>
<country2>: <2nd largest population density in persons/km2>
<country3>: <3rd largest population density in persons/km2>
...
```

2. Like the XML examples, the Module 12 slides show how to process JSON data expressed as a string using the **json.loads()** method. Processing JSON data from a file requires using the **json.load()** method, which takes a single file handle argument and returns a dictionary. For example, if the JSON data in the slides were stored in the file "data.json", we can access the information using the following Python commands:

```
file = open("data.json")
info = json.load(file)
```

We can then use the same commands shown in the slides to process the data.

Let's consider a new problem. The file "gutendex.json" contains meta data about books from Project Gutenberg, an online library of free eBooks. 

Write a program M12_p2.py that reads "gutendex.json", extracts information, and saves it to the file "books.txt". For each book, you must extract information about the book ID, title, author, number of downloads, and URL. The URL will always have the format:

`https://www.gutenberg.org/files/<ID>/<ID>-0.txt,`

where <ID> is the book ID. The following shows the first entry from "books.txt":

```
Title: "Pride and Prejudice"
Author: Austen, Jane
Downloads: 34176
URL: https://www.gutenberg.org/files/1342/1342-0.txt
```
