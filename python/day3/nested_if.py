"""
if condition1: 
    if condition2:
        # Execute this block
    else:
        # Inner condition is false
else: 
    # Outer Condition is false

"""
"""
Create a program that checks whether:
1. The user is logged in.
2. If logged in, check whether the account is active.
3. Allow access only if both conditions are satisfied.

"""

is_logged_in = False
is_active = False

if is_logged_in:
    print("User is Logged in.")
    if is_active:
        print("Access Granted.")
    else: 
        print("Your account is inactive.")
else: 
    print("User not logged in.")

