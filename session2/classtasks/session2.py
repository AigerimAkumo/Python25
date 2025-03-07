

# Numeric Data Type

# - Binary -0b          -----> 01010101
# - Octal - 0o          -----> 0-7
# - Hexidecimal - 0x    ------> 16  --> 0-9 abcdf


# prints 85
# print(0b1010101)

# convert 85 to binary
# print(bin(21))
# print(oct(21))
# print(hex(21))

# word = "Hello "
# print(word * 3)


####### Bolean Data Types

# usage : in if else:

# usage : Operators
#  <
#  <=
#  >
#  >=
#  ==
# !=

# print(10<5)

# inp = int(input("please provide a number: "))

# if inp < 10
#    print("the number is less than 10")
# else:
#     print()   



# class task 1

# take the word input (string)
# find the length of the word
# if length is more than 10
# print("That's a long word")
# else print("The word has {length of the word} characters")

# indentations ---> python syntax
# fstring ---> gives ability to insert variable to your string


# word = input("Please enter a word: ")

# length = len(word)

# if length > 10:
#     print(f"That's a long word! It has {length} characters ")
# else:
#     print(f"The word has {length} characters" )


# Boolean Operators
# not, and , or

# and | or ---> combines 2 or more booleans together
# if num < 10 and num > 0

# and ---> True and True == True
#     ---> False and True == False

# not

# (False and False or not True or True) /False


# class task 2

# Write a program that will do the following
# 1. Takes integer input
# 2. checks if integer is positive 
# 3. checks if the integer is even or odd
# 4. prints the following: "The number is even/odd"

#ex
#num = 10
#output: This number is even

#num = 5
#output: "This number is odd"


num = int(input("enter a number: "))

if num >= 0:
    print("This is positive number")
    if num % 2 == 0:
        print("Even") 
    else:
        print("Odd")
else:
    print("Hey ,this is negative number.please put positive number")    
     

