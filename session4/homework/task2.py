
# Task 2: Remove Duplicates from a List
# Ask the user to enter multiple words separated by spaces. Store them in a list and remove duplicate words while maintaining the original order.
# Example:
# Enter words: apple banana apple cherry banana apple  
# Filtered List: ['apple', 'banana', 'cherry']

inp = input("Please, enter multiple words separated by spaces: ")
user_list = inp.split()

new_list = []

for item in user_list:
    if item not in new_list:
        new_list.append(item)
print (" ".join(new_list))