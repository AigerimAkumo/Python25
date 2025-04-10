

# for <variable for loop> in <sequence>

# for w in "Hello":
#     print(w + "lo")


# print numbers from 1-10
# variable --> 1 = 10
# iteratable --> the value constantly changes

# num = 10 it's just a number 10 .it is nor represent the numbers from 0-9

# range(-10 start, 20 -- end, 2 -- jump )

# for num in range(-10, 20, 2):
#     print(num)


# for num in range(11):
#     if num % 2 == 0:
#        print(num)


# task2
# Character counter

# take an input of the word/sentence
# calculate how many 'a' character are in the word/sentence

# Input :akumosolutions -- a
# OUtput: 1

# Input : banana
# Outout: 3


# word = input("please enter a word: ")
# counter=0

# for char in word:
#     if char == "a":
#         counter = counter + 1
      
# print(counter)



# addition to this task
# instead of taking "a" ,let the user choose the letter
# sentence or character should be case insensative (hint: use lower() or upper() )

word = input("please enter a word: ").lower()
char=input("please enter any character you would like: ").lower()

char_len = len(char)

counter=0
if char_len == 1:
    for b in word:
        if b == char:
            counter=counter + 1

print(counter)


sentence = input("Input: ").lower()
char_inp = input("Input char: ").lower()
char_inp2 = input("Input char 2: ").lower()

counter = 0
counter2 = 0

if len(char_inp) == 1 and len(char_inp2) == 1:
    for char in sentence:
        if char == char_inp:
            counter = counter + 1
        elif char == char_inp2:
            counter2 = counter2 + 1

    print(f"{char_inp} = {counter}")
    print(f"{char_inp2} = {counter2}")

else:
    print("Character input is more than 1")
    
    
    #changed somethign 