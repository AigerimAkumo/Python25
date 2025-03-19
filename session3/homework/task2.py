
# Task 2: Reverse a Word using for loop (please don’t reverse a string using word[::-1])
# Input:
# Enter a word: Python
# Output:
# Reversed Word: nohtyP


word = input("Please enter a word: ")  
reversed = ""  

for n in word:  
                # updating this same variable to build the reversed string
    reversed = n + reversed

print(reversed) 
