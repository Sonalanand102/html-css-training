"""
Problem statement:

Create an electricity bill calculator based on the number of units consumed.

Use these hypothetical rates:
Units consumed - Rate per unit
Up to 100	₹2
101–200	₹3
Above 200	₹5

"""

units_consumed = int(input("Enter units consumed:"))
bill = None

if units_consumed >=0 and units_consumed <=100:
    bill = units_consumed * 2
elif units_consumed >= 101 and units_consumed <200:
    bill = units_consumed * 3
elif units_consumed >=200:
    bill = units_consumed * 5
else:
    print("Invalid input.")

print(bill)