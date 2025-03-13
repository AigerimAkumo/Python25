
# Task 5: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

# word=input("please enter a word: ")

# for n in range(1, len(word) +1):
#     print(word[:n])

inp = input("Input: ") 

for char in range(len(inp)):
    print(inp[:char +1])