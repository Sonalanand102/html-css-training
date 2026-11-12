# Write a program that accepts a number from the user and prints its multiplication table from 1 to 10.

number = 19

for i in range(1,11):
    result = number * i
    print(f"{number} * {i} = {result}")