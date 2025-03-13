
# Task 1: Count Down from input number to 1
# Input: 10
# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

num = int(input("Please enter a number: "))

#              start, breaking point, end
for n in range(num, 0, -1):
   
    print(n)   
