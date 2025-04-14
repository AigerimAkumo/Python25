
def sample(value):
    return total - value

total = 4
total = sample(2)
total = sample(1)
print(total)   # 1



def sample(value):
    return value + value

x = sample(value=1)  
y = sample(x)       
print(y)   # 4


#####################################################################


def comb(w, h=10, d=0, is_d3=False):
    if is_d3:
        return [is_d3, w, h, d]

print(comb(2)[0])  # TypeError because you cannot index into None



##### SOLUTION:
def comb(w, h=10, d=0, is_d3=False):
    if is_d3:
        return [is_d3, w, h, d]

# Set is_d3 to True
result = comb(2, is_d3=True)
print(result[0])  # Output will be True, because is_d3 is set to True


#########################################################################




def walk(top):
    if top == 0:
        return 1 
    else:
        return top * walk(top - 1)

print(walk(2))  #  2




def walk(start, stop=1):
    print(start, end=" ")
    if start + 1 < stop:
        walk(stop, start + 1)

walk(3)  # 3


##########################################################################






def process(data):
    data = [2]  # Return a list instead of a number
    return data

measurements = [0 for i in range(3)]
result = process(measurements)
print(result[-2])   #  2




def process(data):
    data = [2]  # Return a list instead of a number
    return data
measurements = [0 for i in range(3)]
process(measurements)
print(measurements[-2])  # 0



def process(data):
    data = [1, 2, 3]
    return data[-2]  # 2



###########################################################################





list1 = [1, 2]
list2 = list1[:]  # Creates a copy of list1
list2.append(3)   # Appends 3 to the copied list
print(list1[-1])  # Prints the last element of list1
## 2




numbers = [4, 3, 2, 1]
print(numbers[3:5])   # [1]


#############################################################################

train_speed = { 
    "FlyingScotsman": 201, 
    "TGV": 320, 
    "Shinkansen": 320 
}
for train, speed in train_speed.items():  # FlyingScotsman

    if train[0] == "F":
        print(train) 




train_speed = { 
    "FlyingScotsman": 201, 
    "TGV": 320, 
    "Shinkansen": 320 
}
for train in train_speed:
    print(train[0], end="")  # FTS
    
    
    
    
    
    train_speed = { 
    "FlyingScotsman": 201, 
    "TGV": 320, 
    "Shinkansen": 320 
}
for train in train_speed.values():
    print(str(train)[0], end="") # 233
    
    
    
    
###############################################################################    
    
angle = 0

for i in range(5):         # i goes from 0 to 4
    if i % 2 == 0:         # if i is even
        angle += 1
else:
    angle -= 1

print(angle) # OUTPUT 2



angle = 1
for i in range(2, 5):
    if 2 * i > 4:
        angle += 1
else:
    angle -= 1
print(angle)   # 2




################################################################################




power = 1
while power < 5:
    power += 1
    print("@", end="")
    if power == 3:
        break
else:
    print("@") # @@
    

######################################################################

torque = 1
while torque < 2:
    torque *= 2
    print("*", end="")
else:
    print("*") # **
    
    
    
torque = 5
while torque > 0:
    torque -= 3
    print("*", end="")
else:
    print("*") # three   ***



torque = 0
while torque != 0:
    torque //= 3
    print("*", end="")
else:
    print("*") # one  *



####################################################################################


planet = 1

if planet < 0:
    print("#")
elif planet >= 2:
    print("##")
else:
    print("###") #     ###
    
    
    
    
answers = (True, False, True)
selections = answers[2:]
points = 0
for answer in selections[-1:]:
    if answer:
        points += 1
print(points)   #  1



################################################################

others = 0

for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others += 1

print(others) # 3



others = 0

for i in range(2, 4):
    for j in range(-1, 2):
        if i == j:
            others += 1
        else:
            break
print(others)   # 0


#################################################################


# 1**2-4//3     # 0
# 4/2-2**1      # 0
#      1//2+3*4  ===> 12
#      4/2+2**1  ===> 4.0



def do_the_mess(parameter):
    parameter=[variable]
    return parameter

the_list=[x for x in range(0,1)]  # [0]
variable=-2
do_the_mess(the_list)  # 0
print(the_list[0])       # 0

#########################################################


data =[ 'peter', 404, 3.03, 'wellnet', 33.03 ]
print(data-1:3])  # 404, 3.03


data = (( 1, 2),) * 7
print(len(data [3:8]))  # 4

## data = ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))
## (1, 2), (1, 2), (1, 2), (1, 2))


# The pyc file contains ...
# A. a Python interpreter.
# B. Python source code.
# C. compiled Python bytecode.  # C 
# D. a Python compiler.


# Select the true statements: (Choose two.)
# A. You can use keywords as variable names in Python
# B. You can use keywords as function names in Python
# C. You cannot use keywords as variable names in Python   # C
# D. You cannot use keywords as function names in Python   # D

# What do you call a computer program which directly executes instructions written in a programming language?
# A. A compiler
# B. An interpreter
# C. A translator
# Correct Answer: B

# The escape character owes its name to the fact that it:
# A. cannot be caught due to its high speed
# B. escapes from source files into the computer memory
# C. changes the meaning of the character next to it     # C

# What do you call a command-line interpreter which lets you interact with your OS and execute Python commands and scripts?
# A. A console
# B. A compiler
# C. Jython
# D. An editor


# A value returned by the input() function is:
# A. an integer
# B. a float
# C. a string
# Correct Answer: C


# What is true about compilation? (Choose two.)
# A. The code is converted directly into machine code executable by the processor
# B. It tends to be faster than interpretation
# C. It tends to be slower than interpretation
# D. Both you and the end user must have the code
# Correct Answer: A B

# The compiled Python bytecode is stored in files having names ending with:
# A. py
# B. pyb
# C. pyc
# D. pc
# Correct Answer: C



# The print() function is an example of:
# A. a Python built-in function
# B. a user-defined function
# C. an anonymous function
# D. a Python output method
# Correct Answer: A


# A keyword is a word: (Choose two.)
# A. that cannot be used as a variable name
# B. that cannot be used as a function name
# C. is the most important word in the whole program
# Correct Answer: A B


# UTF 8 is ...
# A. the 9th version of the UTF Standard.
# B. a synonym for "byte".
# C. a Python version name.
# D. an encoding form of the Unicode Standard.
# Correct Answer: D

# A complete set of known commands is called:
# A. a machine list
# B. a low-level list
# C. an instruction list
# Correct Answer: C


# What do you call a file containing a program written in a high-level programming language?
# A. A code file
# B. A target file
# C. A machine file
# D. A source file
# Correct Answer: D

# What is source code?
# A. A program written in a high-level programming language
# B. Another name for a source file
# C. Machine code executed by computers
# Correct Answer: A


# The folder created by Python used to store pyc files is named:
# pyc__
# pycfiles__
# pycache__
# D. __cache__
# Correct Answer: C


# If a list passed into a function as an argument, deleting any of its elements inside the function using the del instruction:
# A. will not affect the argument
# B. will cause a runtime error
# C. will affect the argument
# Correct Answer: C


# A function definition:
# A. cannot be placed among other code
# B. may be placed anywhere inside the code after the first invocation
# C. must be placed before the first invocation
# Correct Answer: C


# Which of the following items are present in the function header?
# A. function name
# B. return value
# C. parameter list
# D. function name and parameter list
# Correct Answer: D


# The meaning of the keyword parameter is determined by:
# A. its value
# B. its connection with existing variables
# C. its position within the argument list
# D. the argument's name specified along with its value
# Correct Answer: D

# The part of your code where you think an exception may occur should be placed inside:
# A. the except: branch
# B. the exception: branch
# C. the try: branch
# Correct Answer: C

# The part of your code where the handling of an exception takes place should be placed inside:
# A. the except: branch
# B. the exception: branch
# C. the try: branch
# Correct Answer: A

# How many arguments can the print() function take?
# A. Any number of arguments (excluding zero).
# B. Not more than seven arguments.
# C. Any number of arguments (including zero).
# D. Just one argument.
# Correct Answer: C


# Which of the following statements is false?
# A. The None value can be compared with variables.
# B. The None value can not be used as an argument of arithmetic operators.
# C. The None value may not be used outside functions.
# D. The None value can be assigned to variables.
# Correct Answer: C
