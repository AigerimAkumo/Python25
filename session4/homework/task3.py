
# Task 3: Find the Longest Word in a List
# Ask the user to enter a list of words. Find and print the longest word from the list.
# Example:
# Enter words: Python Java JavaScript C  
# Longest word: JavaScript  

words = input("Please, enter multiple words separated by spaces: ")
user_list = words.split()

longest_word = ""
max_lenght = 0

for word in user_list:
    if len(word) > max_lenght:
        longest_word = word 
        max_lenght = len(word)
print (f"The longest word is : {longest_word}")
