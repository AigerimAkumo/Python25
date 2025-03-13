
# Task 5: Print a Word in a Pyramid Shape
# Input:
# Enter a word: CODE

# Output:
# C
# CO
# COD
# CODE

inp = input("please provide a word: ")

for i in range(1, len(inp) + 1):
    print(inp[:i])