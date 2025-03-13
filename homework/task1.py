
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

inp = int(input("please enter a number: "))

for n in range(inp, 0, -1):
    print(n)
