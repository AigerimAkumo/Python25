

# Task 6: Palindrome Checker
# Ask the user to enter a word and check whether it reads the same forward and backward (e.g., "madam" is a palindrome).

# The answer should return True or False


word = input("please enter a word: ")

if word == word[::-1]:
    print("it's a palindrome! ")
else:
    print("It's not a palindrome!")    