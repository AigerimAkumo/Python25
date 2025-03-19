
# Task 3: Three-Number Maximum
# Take three integer inputs and print the largest one using only if-elif-else conditions.

num1=input("please enter 1 numer: ")
num2=input("please enter 2 numer: ")
num3=input("please enter 3 numer: ")



if num1>num2 and num1>num3:
    print(num1, "largest one")
elif num2>num1 and num2>num3:
    print(num2, "largest one")   
elif num3>num1 and num3>num2:
    print(num3, "largest one")
else:
    print(num1,num2,num3, "these numbers are equal")         