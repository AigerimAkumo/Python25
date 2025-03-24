
# def factorial(n):
#     if n == 1:  # breaking point
#         return 1
#     return n * factorial(n - 1)  # call yourself once again


# # factorial of 5
# # n = 5

# # 5 * 4 * 3 * 2 * 1

# # factorial(4) == 4 * 3 * 2 * 1
# # n = 4
# # 4 * factorial(3)

# # factorial(3)
# # n = 3
# # 3 * 2 * 1


# # factorial(2)
# # n = 2
# 2 * 1

# factorial(1) == 1
# return 1

# print(factorial(5))  # 5 * 4 * 3 * 2 * 1 == 120


# print(list('hello'))

# my_list = [3, 1, -1]
# my_list[-1] = my_list[-2]
# print(my_list)




## 16
# data=((1,2),)*7
# print(len(data[3:8]))


## 18
# tup=(1, )+(1, )
# tup=tup+tup
# print(len(tup))

## 19

# data=(1,2,4,8)
# data=data[-2:-1]
# data=data[-1]
# print(data)

## 21
# data = [1, 2, 3, None, (), [],]
# print(len(data))


## 26
# Original list
# list = ['A', 3, 4, 5, 6]
# print("Original list:", list)

# # Reverse the list in place using list.reverse()
# list.reverse()
# print("Reversed list using list.reverse():", list)


## 27

# data1='1', '2'
# data2=('3', '4')
# print(data1+data2)

## 28
# data = (1, 2, 4, 8)
# data = data[1:-1]
# data = data[0]
# print(data)

# Let's break down the code step by step:

# data = (1, 2, 4, 8)
# Here, data is a tuple: (1, 2, 4, 8).

# data = data[1:-1]
# This slices the tuple starting from index 1 and ending at index -1. So, it extracts the elements between index 1 and index -1, excluding the element at index -1. The result is: (2, 4).

# data = data[0]
# Now, data is a tuple (2, 4). The expression data[0] takes the first element of the tuple, which is 2.

# print(data)
# Finally, the code prints the value of data, which is now 2.


## 29
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])


## 32
# nums=[]
# vals=nums
# vals.append(1)

## 33
# data = {'a': 1, 'b': 2, 'c': 3}
# print(data['a', 'b'])


## 36
# nums = [1,2,3]
# data = (('Peter',) * (len (nums)) - nums [::-1][0])
# print (data)


## 37
# t1 = (1, 4, 9)
# t2 = ('A', 'D', 'Z')
# t3 = (True, False, None)
# t4 = (5.0, 7.5, 9.9)
# t1, t3 = t2, t4
# print(t1)


## 38
# data=()
# print(data.__len__())


## 41
# list = [2, 7, 1, 4]
# print(sorted(list))


## 44
# data=['abc','def','abcde','efg']
# print(max(data))



 # Question 47
# data = [10, 2, 1, 7, 5, 6, 4, 3, 9, 8]

# def find_high_low(nums):
#           nums.sort()
#           return nums[-1], nums[0]
# high, low = find_high_low(data)

# print(('The highest number is {} ' +
# 'and the lowest number is {}.').format(high, low)
# )
# # The highest number is 10 and the lowest number is 1.


## 49

# data=['Peter',' Paul','Mary']
# print(data[int(-1 / 2)])
# Peter



## 50
# data = (1, 2, 3, 4)
# data = data[-2:-1]
# data = data[-1]
# print(data)


## 51
# data={1: 0, 2: 1, 3: 2, 0: 1}
# x=0
# for _ in range(len(data)):
#     x=data[x]
    
# print(x)    
# will be 0


## 52

# list=['Peter','Paul','Mary']
# def list(data): 
#     del data[1]
#     data[1]='Jane'
#     return data
# print(list(list))

        

## 58
a=[1,2,3,4,5]      
print([a[3:0:-1]])  


## 60

# data = {'1': '0', '0': '1'}
# for d in data.values():
#    print(d, end='')
   
   
   
   
## 61
   
# dict = {}
# list = ['a', 'b', 'c', 'd']

# for i in range(len(list)-1):
#     dict[list[i]] = (list[i],)

# for i in sorted(dict.keys()):
#     k = dict[i]

# print(k[0])


## 67
# x=[1,2,3,4,5,6,7,8,9]
# x[::2]=10,20,30,40,50,60
# print(x)


# Question 70
# data = [1, 5, 10, 19, 55, 30, 55, 99]
# data.pop(5)
# data.remove(19)
# data.remove(55)
# data.remove(55)
# print(data)



## 73
# t = (('A', 1), ('B', 2), ('C', 3))
# d = dict(t)
# print(d)


## 76
# x = {(1, 2): 1, (2, 3): 2}
# print(x[1, 2])
#The key `(1, 2)` has an associated value of `1`



# x=1//5+1/5
# print(x)



## 9

# def main(a,b,c,d):
#     value=a+b * c-d
#     return value


## 21
# a=10
# b=20
# c=a>b
# print(not(c))


## 25

# list1=[1,2,3,4]
# list2=[1,2,3,4]
# print(list1 is list2)
# print(list1==list2)


## 27

# nums=[3,73,42,23]
# alphs=['p','p','m','j']
# print(nums is alphs)
# print(nums==alphs)

# nums=alphs

# print(nums is alphs)
# print(nums==alphs)

## 28

# x='Peter'
# y='Peter'
# res= x != y
# print(res)


## 29

# x,y,z=3,2,1
# z,y,x=x,y,z
# print(x,y,z)

## 30
# x=1
# print(++++x)



## 31
# x=23+42
# y='23'+'42'
# z='23'*7


## 34

# res=str(bool(1) + float(12) / float(2))
# print(res)


## 38

# languages=["English","Spanish","Germany"]
# more_languages=["English","Spanish","Germany"]
# extra_languages=more_languages



## 42

# x=2+3*5
# print(x)


## 43
# list1=[1,2,3,4]
# list2=[1,2,3,4]

# print(list1 is list2)
# print(list1==list2)

# list1=list2

# print(list1 is list2)
# print(list1==list2)



## 45
# z=10
# y=0
# x=z>y or z==y

# print(x)


## 46
# x=[0,1,2,]
# x[0], x[2] = x[2], x[0]
# print(x)



## 48
# a=1
# b=0
# a=a^b
# b=a^b
# b=a^b
# print(a,b)



## 49
# a=1
# b=0
# c=a&b
# d=a|b
# e=a^b
# print(c+d+e)



## 52

# x=7
# y=x%2
# y+=1
# print(y)




## 53

# list1=[1,2,3,4]
# list2=[1,2,3,4]

# print(list1 is not list2)
# print(list1 != list2)

# list1=list2

# print(list1 is not list2)
# print(list1 != list2)


## 57

# x=['Peter','Paul','Mary']
# y=['Peter','Paul','Mary']
# print(x is y)

# print('t' in 'Peter')

# x=42
# y=42
# print(x is not y)


## 58

# z=2
# y=1
# x= y < z or z > y and y > z or z < y
# print(x)



## 62
## similar to :
# a=1
# b=0
# a=a^b
# b=a^b
# b=a^b
# print(a,b) 
# # Output: 1 0


# x=0
# y=1
# x=x^y
# y=x^y
# y=x^y
# print(x, y)
# Output: 1 1


## 63
# x="2"
# y=2*x
# print(y)


## 64
# x=input()
# y=int(input())
# print(x*y)



## 65

# x=True
# y=False
# z=False

# if x or y and z:
#     print('TRUE')
# else:
#     print('FALSE')    




## 5
# x=1
# y=2
# x,y,z = x,x,y
# z,y,z = x,y,z
# print(x,y,z)




## 7

# x='\''
# print(len(x))



## 25
# index.py:
# from sys import argv

# print(argv[1] + argv[2])


## 26
# #
# #
# #
# #
# def calc_power(x,y):
#     comment="#return the value"
#     return x ** y # raise x


## 28
# incorrect
# x= '\\\'
# print(len(x))

# correct way
# x = r'\\'
# print(len(x))






## 31
# index.py:
# from sys import argv
# sum=0

# for i in range(2, len(argv)):
#     sum+=float(argv[i])
# print("The average score of {0} is {1:.2f}"
#       .format(argv[1], sum/(len(argv)-2))
#       )    




## 42
# x = r'\\\\'
# print(len(x))



## 43
# x="""
# """
# print(len(x))


## 47
# num=2+3*5
# print(Num)


## 51
# print("Hello!")


## 54
# from sys import argv

# print(argv[0])


## Functiob
## 1
# def funct(data):
#     for d in data[::2]:
#         yield d
# for x in funct('abcdef') :
#     print(x,end='')
# #ace


## 4
# def func(number):
#     return number

# print(func(7))


## 5
# def func(num):
#     res='*'
#     for _ in range(num):
#       res += res
#     return res
# for x in func(2):
#     print(x, end='')


## 7

# def test(x=1, y=2):
#     x=x+y
#     y += 1
#     print(x,y)
    
# test(2,1)    


## 9
# def fun(x,y,z):
#     return x+2 * y+3 * z
# print(fun(0, z=1, y=3))


## 10
# def fun():
#     return True
# x=fun(False)
# print(x)



## 12
# def func(p1,p2):
#     p1=1
#     p2[0]=42
# x=3
# y=[1,2,3]  
# func(x,y)
     
     
# print( x, y[0] )


## 13
# def fun(a, b, c=0):
# A. fun(b=0, a=0)
# C. fun(0, 1, 2)


## 14
# def fun(x):
#     x += 1
#     return x

# x=2
# x=fun(x+1)
# print(x)


## 16
# x=1

# def a(x):
#     return 2*x

# x=2+a(x)
# print(a(x))


## 17
# def a(b,c,d):
#     pass


## 18
# def func1(x):
#     return str(x)

# def func2(x):
#     return str(2*x)


# print(func1(1) + func2(2))


## 19
# v = 1
# def fun():
#      global v
#      v=2
#      return v
# print(v)


## 24
# def func(a, b):
#     return a ** a
# print(func(2))


## 25
# def func1(a):
#     return a ** a

# def func2(a):
#     return func1(a) * func1(a)


# print(func2(2))


## 26
# def fun():
#     return 3

# def add(n):
#     return fun()+n

# print(add(3))



## 29
# def func(x):
#    if x % 2 == 0:
#        return 1
#    else:
#        return 
   
# print(func(func(2)) + 1) 


  
  ## 35
# def fun(x=2, y=3):
#       return x*y
  
# print(fun(y=2))  



## 38

# def function1(a):
#     return None

# def function2(a):
#     return function1(a) * function1(a)
# print(function2(2))


## 39
# data = {}

# def func(d, key, value):
#     d[key] = value
# print(func(data, '1', 'Peter'))    



## 44
# def fun(n):
#     n **= n
#     return n
# print(fun(3))


## 47

# num=1
# def fun():
#     num=3
#     print(num, end=' ')
# fun()
# print(num)
   
   
   
## 50

# def func(item)   :
#     item+=[1]
    
# data=[1,2,3,4]    
# func(data)
# print(len(data))


## 54
# def any():
#     print( var+1, end='')
# var = 1
# any()    
# print(var)



## 55
# def func(x):
#     global y
#     y=x*x
#     return y

# func(2)
# print(y)



## 60
# def fun(n):
#     x=[]
#     for i in range(n):
#         x.append(i)
#     return x

# print(fun(4))    




## 62
# def fun(a,b):
#     return a**a
# print(fun(2))


## 63
# def function(x=0):
#     return x



## 65
# def func(x):
#     if x == 0:
#         return 0
#     return x+func(x-1)

# print(func(3))


## 69
# def fun(inp=2, out=3):
#     return inp*out

# print(fun(out=2))



## 71
# def func(x):
#     if x%2==0:
#         return 1
#     else:
#         return 2
# print(func(func(2)))    



## error handling 
## 2
# try:
#     print(5/0)
#     break
#     # some code that might raise an exception
#     x = 1 / 0  # This will raise a ZeroDivisionError
# except :
#     print("sorry something went wrong")
    
# except (ValueError,ZeroDivisionError):
   
#     print("too bad")



## 8
# num = '7' * '7'
# print(num)



## 12
# foo=(1,2,3)
# foo.index(0)



## 16
# try:
#     raise Exception
# except BaseException:
#     print('1')
# except Exception:
#     print('2')    
# except:
#     print('3')    


## 17
# value = input("enter: ")
# print(10/value)


## Data Types
## 5

# data=eval(input("Input:"))
# print('output: ', data)



## 6
# print(float("1, 3"))


## 8
# x, y = eval(input("Input two num: "))
# print(x)
# print(y)


## 10
# z=y=x=1
# print(x,y,z, sep='*')



## 11
# w=bool(23)
# x=bool('')
# y=bool(' ')
# z=bool([False])



## 16
# x=input("first num: ")
# y=input("second num: ")

# 'The Result is ' + (int(x) + int(y)) tries to concatenate the string 
# 'The Result is ' with the sum of the two integers.
# +
# print('The Result is ' + str(int(x + y)))
# print('The Result is ' + str(int(x) + int(y)))


## 18
# print("Peter's sister's name's \"Anna\"")


## 21
# x=int(input("num1: "))
# y=int(input("num1: "))
# print(x+y)



## 23
# data = ['Peter', 'Paul', 'Mary', 'Jane']
# # print('\n'.join(data))


# print(type(1J))


## 26
# x=(3, )
# print(len(x))


## 28
# print(ord('c') - ord('a'))


## 30
# print(chr(ord('p') + 3))


## 33
# str="Hello World"
# print(str[::-1])


## 38
# print(not 0)
# print(not 23)
# print(not '')
# print(not 'Peter')
# print(not None)



## 40
# substring = 'ab': This means you are searching for the substring 'ab'.
# start = 1: The search starts from index 1 (the second character in the string). 
# The string indexing starts from 0, so the search begins from the second character, 
# which is 'b' in the string 'abbabadaadbbaccdabc'.

# data='abbabadaadbbaccdabcab'
# print(data.count('ab', 1))

# print('Peter' 'Wellert')


# print(float('1.3'))


## 10
# room=input("enter the room number: ")
# # room = int(room)  # Convert the input to an integer
# rooms={101: "gathering place", 102: "meeting room"}
# if not room in rooms:
#     print("the room doesn't exist")
# else:
#     print("the room is: "+rooms[room])    


## 27
# for n in range(1,6,2):
#    print(str(n) * 5)



## 30
# def safe_root(a, b):
#     if a >= 0:
#         answer = a ** (1 / b)
#     elif a % 2 == 0:
#         answer = "result is in imaginary number"
#     else:
#         answer = -(-a) ** (1 / b)
#     return answer


## 33

# data=['Peter','Mary','Paul','Jane']
# res=0

# for i in ('Peter','Steve','Jane'):
#     if i in data:
#         res+=50
# print(res)        


# print(len([i for i in range(0, -2)]))



## 48

# num = 2
# while num <= 100:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime==True:
#         print(num)
#     num += 1


# dict1 = {'one': 1, 'two': 2, 'three': 3}
# dict2 = {'one': 1, 'two': 5, 'four': 8}
# dict3 = dict(dict1)
# dict4 = dict(dict2)
# dict3.update(dict2)
# # dict4.update(dict1)
# # print(dict3 == dict4)

# tup_a = (0, 1, 2)
# tup_b = (2, 3, 4)
# list_c = []
# for el in tup_a:
#         if el not in tup_b:
#                 list_c.append(el)
# print(list_c)


# nums = [1, 2, 3]
# nums[0], nums[2] = nums[2], nums[0]

# x = 4
# y = 5
# z = 3
# print(x == y or z)



# tup_a = (0, 1, 2)
# tup_b = (2, 3, 4,1)
# list_c = []
# for el in tup_a:
#         if el not in tup_b:
#                 list_c.append(el)
# print(list_c)




# list1=[1,3] # 1,3
# list2=list1 # 1,2
# list1[0]=4 # 4,3
# print(list2)