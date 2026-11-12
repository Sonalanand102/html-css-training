"""
1. if

if condition:
    # code executes if condition is true

2. if-else

if condition:
    # Executes when condition is True
else:
    # Executes when condition is False

3. if - elif - else

if condition1:
    # First condition
elif condition2:
    # Second condition
elif condition3:
    # Third condition
else:
    # If all conditions are False
    
"""

percentage = int(input("Enter your percentage:"))

if percentage >= 90 and percentage<=100:
    print("Grade A")
elif percentage >= 75 and percentage <= 90:
    print("Grade B")
elif percentage >=60 and percentage <= 75:
    print("Grade C")
elif percentage >=40 and percentage <= 60:
    print("Grade D")
elif percentage >=0 and percentage <= 40:
    print("Failed")
else:
    print("Invalid Score")