

# Task 1: Number Comparison
# Write a program that takes two integer inputs and prints:
# "Both numbers are equal" if they are the same.
# "The first number is greater" if the first number is larger.
# "The second number is greater" if the second number is larger.


num1 = int(input("please provide fist number: "))
num2 = int(input("please provide second number: "))

if num1 > num2:
    print("The first number is greater")
elif num2 > num1:
    print("The second number is greater")
else:    
    print("Both numbers are equal")