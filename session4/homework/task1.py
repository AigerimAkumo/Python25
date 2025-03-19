
# Here is the tasks for Session 4:
# Note: Please submit your HWs from previous sessions
# Task 1: Reverse a List
# Write a program that reverses a list using a for loop.
# Example:
# # Input:
# Enter numbers separated by space: 1 2 3 4 5
# # Output:
# Reversed List: [5, 4, 3, 2, 1]


inp = input("Please, enter few numbers separated by space: ")
user_list = inp.split()

reversed_list = []

for i in range(len(user_list) -1, -1, -1):
    reversed_list.append(user_list[i])
print (" ".join(reversed_list)) # " " means the space between each element