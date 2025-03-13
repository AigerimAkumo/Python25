# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP

inp = input("please enter a word: ")

reversed_word=""

for n in inp:
    reversed_word = n + reversed_word

print(reversed_word)    