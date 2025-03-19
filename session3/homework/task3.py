# Task 3: Factorial of a Number (use for loop)
# Input:
# Enter a number: 5

# Output:
# Factorial of 5 is 120

num = int (input ("Enter a number: "))
factor = 1
if num >= 1:
      # starts from 1 , 1 and going up to ,it will loop through 1, 2, 3, 4, 5.
    for i in range (1, num+1):
        factor=factor *i
print("Factorial of the given number is: ", factor)