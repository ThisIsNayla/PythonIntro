# Write a program M07_p1.py that asks the user to enter the name of a text file and a word size. 
# The program should print all words in the file that have that size and return the total number of
# words that match the size in an appropriate message. Except for apostrophes, punctuation marks that
# belong to the string: ",.;:?" should not be counted as part of the word length. For example, "day?"
# should be counted as a three-letter word and "wand'rest" should be counted as a 9-letter word. To help 
# you develop your program, a text file (sonnet18.txt) containing Shakespeare's Sonnet 18 will be 
# provided for you.
	
# Example:
# Enter file name: sonnet18.txt
# Enter word length: 9
# temperate
# untrimmed
# wand'rest
# Total words of length 9: 3

file_name = input("Enter file name: ")
word_length = int(input("Enter word length: "))
file = open(file_name)

punctuation = ",.;:?"

count = 0
for line in file:
    for word in line.split():
        word = word.strip(punctuation)
        if len(word) == word_length:
            print(word)
            count += 1

print(f"Total words of length 9: {count}")