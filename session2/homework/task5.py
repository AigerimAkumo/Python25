
# Task 5: Number Type Identifier
# Take a single integer input and classify it as follows:
# If it’s positive and even, print "Positive Even"
# If it’s positive and odd, print "Positive Odd"
# If it’s negative and even, print "Negative Even"
# If it’s negative and odd, print "Negative Odd"
# If it’s zero, print "The number is zero"

num=int(input( "please enter your number: "))

if num >= 0 and num % 2 == 0:
    print("Positive Even")
elif num >= 0 and num % 2 != 0:
    print("Positive Odd")  
elif num < 0 and num % 2 == 0:
    print("Negative Even")
elif num < 0 and num % 2 != 0:
    print("Negative Odd")    
else:
    print("The number is zero")    
 
     