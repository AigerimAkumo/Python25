
# Task 4: Password Verification (Limited Attempts)
# secret password = Python123
# Input:

# Enter the password: hello
# Wrong password. Try again.

# Enter the password: python
# Wrong password. Try again.

# Enter the password: Python123
# Access Granted!


secret_password = "Python123"

max_attempts=3

for attempt in range(max_attempts):

    entered_passw=input("enter your password: ")

    if entered_passw == secret_password:
        print("Access Granted!")
        break
    else:
        print("Wrong password. Try again.")    

else:
  print("You have reach the limit of attempting")
