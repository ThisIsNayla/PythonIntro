# 	2. Write a program M9_p2.py that reads a user-specified text file and uses a dictionary to 
# print all duplicate words in the file and their corresponding counts. A word is a duplicate if 
# it appears more than once in the file. Your program should not consider punctuation marks (,.;?!:)
# to be part of a word. It should also treat words in uppercase or lowercase letters as being the same. 
# For example, the words "The" and "the" should be treated as being identical. Use the sorted() 
# function to sort the dictionary alphabetically before printing duplicate words.

# Example: 
# Enter file name: sonnet18.txt 
# Duplicate words:
# a 2 
# and 5 
# can 2 
# eternal 2
# …

file_name = input("Enter file name: ")
file = open(file_name)

words = {}
count = 0

for line in file:
    for word in line.split():
        w = (word.lower().strip(",.;?!:"))
        if w not in words:
            words[w] = 1
        else:
            words[w] += 1

print("Duplicate words:")
for word in sorted(words):
    if words[word] > 1:
        print(word, words[word])