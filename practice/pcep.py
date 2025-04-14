


# print(1//2+3*4)
# 
# 4/2+2**1


# torque=1
# while torque < 2:
#     torque *= 2
#     print("*", end="")
# else:
#     print("*")    


# planets= 1+1 // 2*3


# others=0

# for i in range(2):
#     for j in range(2):
#         if i != j:
#             others += 1
# else:
#     others += 1
# print(others)                


# power=1
# while power < 5:
#     power += 1
#     print("@", end="")
#     if power == 3:
#         break
# else:
#     print("@")    

# Initialization:

# power is initially set to 1.

# First iteration of the while loop:

# Condition check: power < 5 → 1 < 5 is True, so the loop starts.

# power is incremented by 1: power = 1 + 1 = 2.

# The print("@", end="") statement prints @ without a newline, so @ is printed on the same line.

# The if power == 3 condition is checked: power == 3 is False, so no break occurs.

# Second iteration of the while loop:

# Condition check: power < 5 → 2 < 5 is True, so the loop continues.

# power is incremented by 1: power = 2 + 1 = 3.

# The print("@", end="") statement prints another @.

# The if power == 3 condition is checked: power == 3 is True, so the loop breaks at this point.


# angle=0
# for i in range(5):
#     if i %2 == 0:
#         angle += 1
# else:
#     angle -= 1
# print(angle)            


# Step-by-Step Execution:
# Initialization:

# angle is initially set to 0.

# For loop (for i in range(5)):

# The range(5) produces values 0, 1, 2, 3, 4 for i.

# The loop will iterate 5 times, once for each of these values of i.

# Iteration 1 (i = 0):

# Condition check: i % 2 == 0 → 0 % 2 == 0, which is True.

# Since the condition is True, angle += 1 is executed: angle = 0 + 1 = 1.

# Iteration 2 (i = 1):

# Condition check: i % 2 == 0 → 1 % 2 == 1, which is False.

# Since the condition is False, angle remains unchanged: angle = 1.

# Iteration 3 (i = 2):

# Condition check: i % 2 == 0 → 2 % 2 == 0, which is True.

# Since the condition is True, angle += 1 is executed: angle = 1 + 1 = 2.

# Iteration 4 (i = 3):

# Condition check: i % 2 == 0 → 3 % 2 == 1, which is False.

# Since the condition is False, angle remains unchanged: angle = 2.

# Iteration 5 (i = 4):

# Condition check: i % 2 == 0 → 4 % 2 == 0, which is True.

# Since the condition is True, angle += 1 is executed: angle = 2 + 1 = 3.

# Else block:

# After the loop finishes, the else block is executed.

# angle -= 1 is executed: angle = 3 - 1 = 2.

# Final Output:
# After completing the loop and the else block, the value of angle is 2.



# train_speed= { "FlyingScotsman":201, "TGV":320, "Shinkansen": 320 }
# for train in train_speed.values():
#     print(str(train) [0], end="")
    
#     Step-by-Step Execution:
# First, train = 201: str(201)[0] gives "2".

# Then, train = 320: str(320)[0] gives "3".

# Finally, train = 320 again: str(320)[0] gives "3".


# answers = (True,False,True)
# selections=answers[2:]
# points=0
# for answer in selections[-1:]:
#     if answer:
#         points += 1
# print(points)        


# numbers = [4,3,2,1]
# print(numbers[3:5])

# def process(data):
#     data=[1,2,3]
#     return data[-2]

# measurements= [0 for i in range(3) ]
# process(measurements)
# print(measurements[-2])


# def walk(start, stop=1):
#     print(start, end=" ")
#     if start + 1 < stop:
#         walk(stop, start + 1)
# walk(3)        


# planet = 4-3 // 2+ -1

# if planet < 0:
#     print("#")
# elif planet >= 2:
#     print("##")  
# else:
#     print("###")      



# list1=[1,2]
# list2=list1[:]
# list2.append(3)
# print(list1[-1])

# angle = 1
# for i in range(2, 5):
#     if 2 * i > 4:
#         angle += 1
# else:
#     angle -= 1
# print(angle)            


# def sample(value):
#     return value+value

# x=sample(value=1)
# y=sample(x)
# print(y)


# def process(data):
#     data = 2
#     return data

# measureents = [0 for i in range(3)]
# result=process(measureents)
# print(result[-2])

# def walk(top):
#     if top==0:
#         return 0
#     else:
#         return top*walk(top-1)
# print(walk(2))    


# def comb(w,h=10,d=0,is_d3=False):
#     if is_d3:
#         return [is_d3,w,h,d]
# print(comb(2) [0])



# others=0

# for i in range(2, 4):
#     for j in range(-1, 2):
#         if i==j:
#             others+=1
#         else:
#             break
# print(others)        



# def sample(value):
#     return total-value


# total=4
# total=sample(2)
# total=sample(1)
# print(total)



## A binary code is code designed to be executed by hardware (the CPU) and hence this kind of code is actually 
# a sequence of bits which forms a series of machine instructions.

## a sequence of bits which encodes machine instructions








# x=0
# while x < 6:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print('*') #three



# x=0
# while x < 6:
#     x += 1
#     if x % 2 == 0:
#         break
#     print('*') # one



# n=1
# if n==1:
#     print('*')
# if n==True:
#     print('**')
# if n==False:
#     print('***')        #two
    
    
    
    
#    Arrange the code boxes in the correct positions in order to obtain a loop which executes 
# its body with the level variable going through values 5, 3 ,
# and 1 (in the same order).


# total=0
# for i in range(4):
#     if 2 * i > 4:
#         total+=1
#     else:
#         total+=1
#     print(total)        # 4
    
   
    
# total = 0
# for i in range(4):         # i = 0, 1, 2, 3
#     if 2 * i >= 4:         # now true for i = 2 and 3
#         total += 1
# print(total)               # prints 2
    
    
# def velocity(x)  :
#   return speed + x

# speed=10
# new_speed=velocity(10)
# new_speed=velocity(speed)
# print(new_speed) # 20
