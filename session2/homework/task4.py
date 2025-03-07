
# Task 4: Password Strength Checker
# Ask the user for a password input. Check and print:
# "Strong password" if the length is at least 8 characters and contains both letters and numbers.
# "Weak password" otherwise.


passw=input("please enter your password: ")

characters=len(passw)
a=int(0-9)
b=str("a-z")

if characters >= 8:
    print("Strong Password! ")
    if characters==a and characters==b:
        print("you good to go! Strong password!")
else:
    print("Weak Password!")    