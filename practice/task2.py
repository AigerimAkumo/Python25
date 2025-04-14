
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


def velocity(x)  :
  return speed + x

speed=10
new_speed=velocity(10)
new_speed=velocity(speed)
print(new_speed)        #20


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



def runner(brand, model="", year=2021, convertible=True):
    return brand + model + str(convertible)

print(runner("Volta", "Tension", 2019)[-1])    # [-1] returns e




def runner(brand, model="", year=2021, convertible=True):
    return brand  # Only return the brand

print(runner("Volta", "Tension", 2019))     # Volta




def runner(brand, model="", year=2021, convertible=True):
    return brand + " " + model + " " + str(year)

print(runner("Volta", "Tension", 2019))     # Volta Tension 2019




def runner(brand, model="", year=2021, convertible=True):
    return convertible

print(runner("Volta", "Tension", 2019, False))      # False



    
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

speed = 3
while speed < 0:
    speed **= 2
    if speed == 7:
        break
    print('*', end="")
else:
    print("*")  # *




power = 1
while power < 5:
    power += 1
    print("@", end="")
    if power == 3:
        break
else:
    print("@") # @@




floor = 10
while floor != 0:
    floor //= 4
    print("#", end="")
else:
    print("#") # ###



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

for i in range(2):
    for j in range(2):
        if i == j:
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





def do_the_mess(parameter):
    global variable
    variable += parameter[0]
    return variable

the_list=[x for x in range(2, 3)] 
variable= 0
do_the_mess(the_list) 
print(variable)         # 2




#########################################################


data =[ 'peter', 404, 3.03, 'wellnet', 33.03 ]
print(data-1:3])  # 404, 3.03

###########################################################

data = (( 1, 2),) * 7
print(len(data [3:8]))  # 4

## data = ((1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2))
## (1, 2), (1, 2), (1, 2), (1, 2))



collection = []
collection.append(1)
collection.insert(0,2)
duplicate = collection
duplicate.append(3)
print(len(collection) + len(duplicate)) # 6


def iterate(end,foo = 0):
    if end > 0:
        foo = iterate(end-1, foo+end)
        return foo
print(iterate(2))        # Output: 3



##############################################################

rates = (1.2, 1.4, 1.0)
new = rates[3:]
for rate in rates[-2:]:
    new+=(rate,)
print(len(new))    # 2

# You started with an empty tuple new.
# Then you added the last two elements of rates to new.
# The length of the final tuple is 2.


##############################################################

# Which of the following functions can be invoked without arguments?

# A. def gamma(level):
This function expects 1 value called level.

❌ You cannot run it without arguments.

❌ You cannot run it with 2 arguments (it only takes 1).

# pass


# B. def delta(level, size = 0):
This function expects at least 1 value: level.

size is optional (because it has a default =0)

✅ You can call it with 2 arguments.

❌ You cannot call it with 0 arguments.
    
# pass

    
# C. def alpha (level=100):
level has a default value, so it's optional.

✅ You can call it without arguments.

❌ You cannot call it with 2 arguments (only 1 parameter exists).    
# pass


B (delta(level, size=0))
C (alpha(level=100))



# What is true about exceptions in Python? (Choose two.)
# A. Not more than one except branch can be executed inside one try-except block.
# B. According to Python terminology, exceptions are raised.
# C. According to Python terminology, exceptions are thrown.
# D. Python’s philosophy encourages developers to make all possible efforts to protect the program from the occurrence of an exception.
# Correct Answer: B D

