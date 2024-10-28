# A palindrome is a word that reads the same from either end. For example, "civic", "radar", 
# and "madam" are palindromes, while "tree", "car", and "horse" are not. Write a program M06_p3.py 
# that asks the user to enter a word and checks if the word is a palindrome. Note that single-letter 
# words are allowed and should be considered palindromes.  
	
# 	Example:  
# 	Enter a word: civic 
# 	civic is a palindrome.  
	
# 	Enter a word: tree 
#   tree is not a palindrome.  

word = str(input("Enter a word: "))
if word[::] == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")